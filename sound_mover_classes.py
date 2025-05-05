from dataclasses import dataclass, field
from io import BufferedReader
import struct

@dataclass
class Vab:
    name: str
    vh_path: str = None
    vb_path: str = None
    is_ae: bool = None
    sound_file: BufferedReader = None

    def __post_init__(self) -> None:
        self.vb_records: list[VbRecord] = []
        self.vh_header: VhHeader = None
        self.vh_program_records: list[VhProgramRecord] = []
        self.vh_tone_records: list[VhToneRecord] = []

        if self.vh_path:
            self.read_vh(self.vh_path)
        if self.vb_path:
            self.read_vb(self.vb_path, self.sound_file)
    
    def read_vh(self, vh_path: str | BufferedReader) -> None:
        if not vh_path:
            return

        with open(vh_path, "rb") as vh_file:
            buff = vh_file.read(32)
            if len(buff) != 32:
                return
                
            self.vh_header = VhHeader(self, *struct.unpack("4s3iH3h4bi", buff))

            # read program records
            for i in range(128):
                buff = vh_file.read(16)
                if len(buff) != 16:
                    raise Exception("Unexpected end of VH")
                program_record = VhProgramRecord(self, i, *struct.unpack("6bh2i", buff))
                
                # if program_record.tone_count == 0 or program_record.volume == 0:
                    # continue
                self.vh_program_records.append(program_record)
            
            # read tone records
            for _ in range(self.vh_header.program_count * 16):
                buff = vh_file.read(32)
                if len(buff) != 32:
                    raise Exception("Can't read VH - invalid program count")
                    
                tone_record = VhToneRecord(self, *struct.unpack("16B2H2h4H", buff))
                
                if tone_record.wave == 0:
                    continue
                    
                tone_record.wave -= 1
                self.vh_tone_records.append(tone_record)

        
        for vh_tone in self.vh_tone_records:
            self.vh_program_records[vh_tone.program].tones.append(vh_tone)
        
        return (self.vh_program_records, self.vh_tone_records)
    
    def read_vb(self, vb_path: str, sounds_file: BufferedReader = None):
        if not vb_path:
            return

        # print(vb_path)
        with open(vb_path, "rb") as vb_file:
            read_len = 12 if sounds_file else 8
            index = 0
            while True:
                data = vb_file.read(read_len)
                
                if len(data) != read_len:
                    break
                
                vb_record = None
                
                if self.is_ae:
                    vb_record = VbRecord(self, index, *struct.unpack("3i", data))
                    sounds_file.seek(vb_record.offset, 0)
                    vb_record.sound_data = sounds_file.read(vb_record.length)
                else:
                    vb_record = VbRecord(self, index, *struct.unpack("2i", data))
                    vb_record.sound_data = vb_file.read(vb_record.length)
                
                self.vb_records.append(vb_record)
                index += 1
                # print(f"{length} {sample_rate} {offset}")
        return self.vb_records

    def write_vh(self, path: str = None):
        path = path or self.vh_path 
        if path is None:
            return

        print(f"Writing {path}")
        with open(path, "wb") as vh_file:
            vh_file.write(struct.pack("4s3iH3h4bi",
                self.vh_header.magic, self.vh_header.version, self.vh_header.id, self.vh_header.size, self.vh_header.reserved,
                self.vh_header.program_count, self.vh_header.tone_count, self.vh_header.wave_count, self.vh_header.volume,
                self.vh_header.panning, self.vh_header.attribute1, self.vh_header.attribute2, self.vh_header.reserved2))

            for vh_rec in self.vh_program_records:
                vh_file.write(struct.pack("6bh2i",
                    vh_rec.tone_count, vh_rec.volume, vh_rec.priority, vh_rec.mode, vh_rec.panning,
                    vh_rec.reserved1, vh_rec.attribute, vh_rec.reserved2, vh_rec.reserved3))

            for vh_rec in self.vh_program_records:
                tones = [tone for tone in self.vh_tone_records if tone.program == vh_rec.index]
                if len(tones) == 0:
                    continue

                for vh_tone in tones:
                    vh_file.write(struct.pack("16B2H2h4H",
                        vh_tone.priority, vh_tone.mode, vh_tone.volume, vh_tone.panning, vh_tone.root_note, vh_tone.pitch_shift, vh_tone.min_note, vh_tone.max_note,
                        vh_tone.vibrato_width, vh_tone.vibrato_time, vh_tone.portamento_width, vh_tone.portamento_time, vh_tone.min_pitch_bend, vh_tone.max_pitch_bend,
                        vh_tone.reserved1, vh_tone.reserved2, vh_tone.adsr1, vh_tone.adsr2, vh_tone.program, vh_tone.wave + 1,
                        vh_tone.reserved3, vh_tone.reserved4, vh_tone.reserved5, vh_tone.reserved6))

                empty_tones = 16 - len(tones)
                if empty_tones > 0:
                    vh_tone = VhToneRecord.empty_record(self, vh_rec.index)
                    for _ in range(empty_tones):
                        vh_file.write(struct.pack("16B2H2h4H",
                            vh_tone.priority, vh_tone.mode, vh_tone.volume, vh_tone.panning, vh_tone.root_note, vh_tone.pitch_shift, vh_tone.min_note, vh_tone.max_note,
                            vh_tone.vibrato_width, vh_tone.vibrato_time, vh_tone.portamento_width, vh_tone.portamento_time, vh_tone.min_pitch_bend, vh_tone.max_pitch_bend,
                            vh_tone.reserved1, vh_tone.reserved2, vh_tone.adsr1, vh_tone.adsr2, vh_tone.program, vh_tone.wave,
                            vh_tone.reserved3, vh_tone.reserved4, vh_tone.reserved5, vh_tone.reserved6))
    
    def write_vb(self, path: str = None):
        path = path or self.vb_path 
        if path is None:
            return

        print(f"Writing {path}")
        with open(path, "wb") as vb_file:
            for vb_record in self.vb_records:
                if self.is_ae:
                    vb_file.write(struct.pack("3i", vb_record.length, vb_record.sample_rate, vb_record.offset))
                else:
                    vb_file.write(struct.pack("2i", vb_record.length, vb_record.sample_rate))
                    vb_file.write(vb_record.sound_data)

    def add_tone_record(self, record: 'VhToneRecord') -> tuple[bool, str]: # TODO make this raise exceptions instead of returning success bool and error string
        if not record:
            return (False, "Record can't be None")
        
        if self == record.vab:
            return (False, "Can't add a Tone record from the same VAB.")

        if self.is_ae != record.vab.is_ae:
            return (False, "Can't add a Tone record from a different game.")

        repeats = [x for x in self.vh_tone_records if x.program == record.program and x.min_note == record.min_note and x.max_note == record.max_note]
        if repeats:
            return (False, "This VAB already contains a Tone record with the same program/notes combo.")

        if self.vh_program_records[record.program].tone_count >= 16:
            return (False, "This tone's program in this VAB is full (already contains 16 tone records).")

        # TODO some other checks?

        wave_id = 0
        wave_exists = [x for x in self.vb_records if x.sound_data == record.vab.vb_records[record.wave]]
        if wave_exists:
            wave_id = wave_exists[0].index
            print("found wave")
        else:
            print("moving wave")
            wave_id = len(self.vb_records)
            self.vh_header.wave_count += 1
            cloned_vb = record.vab.vb_records[record.wave].clone(self)
            cloned_vb.index = wave_id
            self.vb_records.append(cloned_vb)

        self.vh_header.tone_count += 1
        if self.vh_program_records[record.program].tone_count == 0: # TODO for remove_tone_record remember to do the reverse
            print("new program")
            self.vh_header.program_count += 1
            self_prg = self.vh_program_records[record.program]
            other_prg = record.vab.vh_program_records[record.program]
            self_prg.volume = other_prg.volume
            self_prg.priority = other_prg.priority
            self_prg.mode = other_prg.mode
            self_prg.panning = other_prg.panning
            self_prg.reserved1 = other_prg.reserved1
            self_prg.attribute = other_prg.attribute
            self_prg.reserved2 = other_prg.reserved2
            self_prg.reserved3 = other_prg.reserved3
        self.vh_program_records[record.program].tone_count += 1
        cloned = record.clone(self)
        cloned.wave = wave_id
        self.vh_tone_records.append(cloned)
        self.vh_program_records[record.program].tones.append(cloned)
        
        return (True, "")

    def remove_tone_record(self, record: 'VhToneRecord') -> tuple[bool, str]: # TODO make this raise exceptions instead of returning success bool and error string
        if not record:
            return (False, "Record can't be None")
        
        if self != record.vab:
            return (False, "Provided tone record is from a different VAB.")

        repeats = [x for x in self.vh_tone_records if x == record]
        if not repeats:
            return (False, "This VAB doesn't contain this tone.")

        for tone in repeats:
            self.vh_tone_records.remove(tone)
            self.vh_header.tone_count -= 1
            self.vh_program_records[record.program].tones.remove(tone)
            self.vh_program_records[record.program].tone_count -= 1
            if self.vh_program_records[record.program].tone_count == 0:
                self.vh_header.program_count -= 1
                prog = self.vh_program_records[record.program]
                prog.volume = 0
                prog.priority = -1
                prog.mode = -1
                prog.panning = 0
                prog.reserved1 = -1
                prog.attribute = -1
                prog.reserved2 = -1
                prog.reserved3 = -1
            
            wave_references = [x for x in self.vh_tone_records if x.wave == record.wave]
            if not wave_references:
                print("removing unused vb sound")
                self.vb_records.remove(self.vb_records[record.wave])
                self.vh_header.wave_count -= 1
                for wave in [x for x in self.vb_records if x.index > record.wave]:
                    wave.index -= 1
                for tone in [x for x in self.vh_tone_records if x.wave > record.wave]:
                    tone.wave -= 1

        #raise Exception("implementation not finished")
        return (True, "")

@dataclass
class VhHeader:
    vab: Vab = field(repr=False, hash=False, compare=False)
    magic: str
    version: int
    id: int
    size: int
    reserved: int
    program_count: int
    tone_count: int
    wave_count: int
    volume: int
    panning: int
    attribute1: int
    attribute2: int
    reserved2: int
        
    # TODO add/remove program

@dataclass
class VhProgramRecord:
    vab: Vab = field(repr=False, hash=False, compare=False)
    index: int
    tone_count: int
    volume: int
    priority: int
    mode: int
    panning: int
    reserved1: int
    attribute: int
    reserved2: int
    reserved3: int

    def __post_init__(self):
        self.tones: list[VhToneRecord] = []

    def __str__(self):
        return f"{self.index},\t{self.tone_count},\t{self.volume},\t{self.priority},\t{self.mode},\t{self.panning},\t{self.attribute}"
        
    # TODO add/remove tone

@dataclass
class VhToneRecord:
    vab: Vab = field(repr=False, hash=False, compare=False)
    priority: int
    mode: int
    volume: int
    panning: int
    root_note: int
    pitch_shift: int
    min_note: int
    max_note: int
    vibrato_width: int
    vibrato_time: int
    portamento_width: int
    portamento_time: int
    min_pitch_bend: int
    max_pitch_bend: int
    reserved1: int
    reserved2: int
    adsr1: int
    adsr2: int
    program: int
    wave: int
    reserved3: int
    reserved4: int
    reserved5: int
    reserved6: int
    global_wave: int = None

    @staticmethod
    def empty_record(vab: Vab, program: int) -> 'VhToneRecord':
        return VhToneRecord(vab, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xB1, 0xB2, 0x80FF, 0x5FC0, program, 0, 0x00C0, 0x00C1, 0x00C2, 0x00C3)

    def clone(self, new_vab: Vab) -> 'VhToneRecord':
        if self.vab == new_vab:
            pass # TODO raise exception?
        return VhToneRecord(new_vab, self.priority, self.mode, self.volume, self.panning, self.root_note, self.pitch_shift, self.min_note, self.max_note,
            self.vibrato_width, self.vibrato_time, self.portamento_width, self.portamento_time, self.min_pitch_bend, self.max_pitch_bend,
            self.reserved1, self.reserved2, self.adsr1, self.adsr2, self.program, self.wave, self.reserved3, self.reserved4, self.reserved5, self.reserved6)

@dataclass
class VbRecord:
    vab: Vab = field(repr=False, hash=False, compare=False)
    index: int
    length: int
    sample_rate: int
    offset: int = None
    sound_data: bytes = None
    loop_start: int = 0
    loop_end: int = 0

    def clone(self, new_vab: Vab) -> 'VbRecord':
        if self.vab == new_vab:
            pass # TODO raise exception?
        return VbRecord(new_vab, self.index, self.length, self.sample_rate, self.offset, self.sound_data, self.loop_start, self.loop_end)
