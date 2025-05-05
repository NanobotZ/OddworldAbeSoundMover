from os import path
import FreeSimpleGUI as sg

from sound_mover_classes import *
from sound_mover_constants import *

class GuiMain:
    def __init__(self):
        self.target_vh_path: str = None
        self.source_vh_path: str = None
        self.sound_file_path: str = None
        self.target_vab: Vab = None
        self.source_vab: Vab = None
        self.target_filter: str = ""
        self.source_filter: str = ""

        target_layout = [
            [sg.Text(text="Target .VH file")],
            [sg.InputText(readonly=True, expand_x=True, key="-TARGET-PATH-"), sg.Button(button_text="Browse", key="-BROWSE-TARGET-")], # TODO add reload button
            [sg.Text(text="Filter")],
            [sg.InputText(enable_events=True, expand_x=True, key="-TARGET-FILTER-")],
            [sg.Listbox(values=[], expand_x=True, expand_y=True, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key="-TARGET-LISTBOX-")]
        ]

        center_layout = [
            [sg.Button("<", key="-MOVE-TO-TARGET-")],
            [sg.Button(">", key="-MOVE-TO-SOURCE-")]
        ]

        source_layout = [
            [sg.Text(text="Source .VH file")],
            [sg.InputText(readonly=True, expand_x=True, key="-SOURCE-PATH-"), sg.Button(button_text="Browse", key="-BROWSE-SOURCE-")], # TODO add reload button
            [sg.Text(text="Filter")],
            [sg.InputText(enable_events=True, expand_x=True, key="-SOURCE-FILTER-")],
            [sg.Listbox(values=[], expand_x=True, expand_y=True, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key="-SOURCE-LISTBOX-")]
        ]

        layout = [
            [sg.Text(text="Sounds.dat file path (if Abe's Exoddus)")],
            [sg.InputText(readonly=True, expand_x=True, key="-SOUNDS-PATH-"), sg.Button(button_text="Browse", key="-BROWSE-SOUNDS-")],
            [
                sg.Column(layout=target_layout, expand_x=True, expand_y=True),
                sg.Column(layout=center_layout, pad=0, vertical_alignment="center"),
                sg.Column(layout=source_layout, expand_x=True, expand_y=True)
            ],
            [sg.Button(button_text="Save", key="-SAVE-")]
        ]

        sg.theme("DarkGrey8")
        self.window = sg.Window(title="Abe Sound Mover", layout=layout, size=(1200, 800), resizable=True, finalize=True)
        self.main()


    def main(self):
        while True:
            event, values = self.window.read()            
            if event == sg.WIN_CLOSED:
                break
            if event == "-BROWSE-SOUNDS-":
                self.selected_sound_file(sg.popup_get_file("Enter the sound file", file_types=(("Sounds.dat", "sounds.dat"),)))
            if event == "-BROWSE-TARGET-":
                self.selected_target_vh_file(sg.popup_get_file("Enter the target .VH file", file_types=(("VH files", "*.vh"),)))
            if event == "-BROWSE-SOURCE-":
                self.selected_source_vh_file(sg.popup_get_file("Enter the source .VH file", file_types=(("VH files", "*.vh"),)))
            if event == "-TARGET-FILTER-":
                self.filter_target(values["-TARGET-FILTER-"])
            if event == "-SOURCE-FILTER-":
                self.filter_source(values["-SOURCE-FILTER-"])
            if event == "-MOVE-TO-TARGET-":
                self.move_to_target(values["-SOURCE-LISTBOX-"])
            if event == "-MOVE-TO-SOURCE-":
                self.remove_from_target(values["-TARGET-LISTBOX-"])
            if event == "-SAVE-":
                self.save_target_vab()

        self.window.close()
        
    def selected_sound_file(self, result: str):
        if not result:
            return

        if not path.isfile(result):
            return

        self.sound_file_path = result
        self.window["-SOUNDS-PATH-"].update(result)
        self.load_vabs()

    def selected_target_vh_file(self, result: str):
        if not result:
            return

        if not path.isfile(result):
            return

        # TODO make sure game is the same - vab's is_ae

        self.target_vh_path = result
        self.window["-TARGET-PATH-"].update(result)
        self.load_vabs()

    def selected_source_vh_file(self, result: str):
        if not result:
            return

        if not path.isfile(result):
            return

        # TODO make sure game is the same - vab's is_ae
        
        self.source_vh_path = result
        self.window["-SOURCE-PATH-"].update(result)
        self.load_vabs()
    
    def load_vabs(self):
        if not self.target_vh_path or not self.source_vh_path:  # TODO load both VABs seperately, so that switching a source vab doesn't clear changes to the target
            return

        self.unload_vabs()
        
        try:
            sound_file = None
            if self.sound_file_path:
                sound_file = open(self.sound_file_path, "rb")

            target_vab = Vab(None, self.target_vh_path, self.target_vh_path.replace(".VH", ".VB").replace(".vh", ".vb"), True if sound_file else False, sound_file)
            source_vab = Vab(None, self.source_vh_path, self.source_vh_path.replace(".VH", ".VB").replace(".vh", ".vb"), True if sound_file else False, sound_file)

            self.target_vab = target_vab
            self.source_vab = source_vab
        except Exception as ex:
            print(repr(ex)) # TODO display message
            return

        self.populate_target_listview()
        self.populate_source_listview()

    def unload_vabs(self):
        if not self.target_vab or not self.source_vab:
            return

        self.target_vab = None
        self.source_vab = None

        self.window["-TARGET-LISTBOX-"].update(values=[])
        self.window["-SOURCE-LISTBOX-"].update(values=[])

    def populate_target_listview(self):
        listbox: sg.Listbox = self.window["-TARGET-LISTBOX-"]
        items = []
        for vh_tone in sorted(self.target_vab.vh_tone_records, key=lambda r: (r.program, r.min_note, r.max_note)):
            if vh_tone.min_note != vh_tone.max_note:
                continue

            filter = self.target_filter
            text = SOUNDS_MAPPING_AE.get((vh_tone.program, vh_tone.min_note)) if self.target_vab.is_ae else SOUNDS_MAPPING_AO.get((vh_tone.program, vh_tone.min_note))
            if not text or not filter in text.lower():
                continue

            vh_tone.text = text

            items.append(text)

        listbox.update(values=items)

    def populate_source_listview(self):
        listbox: sg.Listbox = self.window["-SOURCE-LISTBOX-"]
        items = []
        for vh_tone in sorted(self.source_vab.vh_tone_records, key=lambda r: (r.program, r.min_note, r.max_note)):
            if vh_tone.min_note != vh_tone.max_note:
                continue

            if (vh_tone.program, vh_tone.min_note) in [(vh_tone2.program, vh_tone2.min_note) for vh_tone2 in self.target_vab.vh_tone_records if vh_tone2.min_note == vh_tone2.max_note]:
                continue
            
            filter = self.source_filter
            text = SOUNDS_MAPPING_AE.get((vh_tone.program, vh_tone.min_note)) if self.source_vab.is_ae else SOUNDS_MAPPING_AO.get((vh_tone.program, vh_tone.min_note))
            if not text or not filter in text.lower():
                continue

            vh_tone.text = text

            items.append(text)

        listbox.update(values=items)

    def filter_target(self, text: str):
        filter = text.lower()
        self.target_filter = filter
        self.populate_target_listview()
                
    def filter_source(self, text: str):
        # self.populate_source_listview()
        filter = text.lower()
        self.source_filter = filter
        self.populate_source_listview()

    def move_to_target(self, values: list[str]):
        any = False

        for item in values:
            tone = [tone for tone in self.source_vab.vh_tone_records if self.get_text_for_tone(tone) == item][0]
            success, err = self.target_vab.add_tone_record(tone)
            if not success:
                sg.Popup(err, title=self.get_text_for_tone(tone), icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING, button_type=sg.POPUP_BUTTONS_OK)
                print(err) # TODO instead show error popup and return
                continue

            any = True
        
        if not any:
            return

        self.populate_target_listview()
        self.populate_source_listview()

    def remove_from_target(self, values: list[str]):
        any = False

        for item in values:
            tone = [tone for tone in self.target_vab.vh_tone_records if self.get_text_for_tone(tone) == item][0]
            success, err = self.target_vab.remove_tone_record(tone)
            if not success:
                sg.Popup(err, title=self.get_text_for_tone(tone), icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING, button_type=sg.POPUP_BUTTONS_OK)
                print(err) # TODO instead show error popup and return
                continue

            any = True
        
        if not any:
            return

        self.populate_target_listview()
        self.populate_source_listview()

    def save_target_vab(self):
        if not self.target_vab:
            return

        self.target_vab.write_vh()
        self.target_vab.write_vb()
        # TODO print success?

    def get_text_for_tone(self, tone: VhToneRecord):
        return SOUNDS_MAPPING_AE.get((tone.program, tone.min_note)) if tone.vab.is_ae else SOUNDS_MAPPING_AO.get((tone.program, tone.min_note))

if __name__ == '__main__':
    GuiMain()