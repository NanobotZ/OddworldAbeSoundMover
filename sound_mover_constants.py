SOUNDS_MAPPING_AO: dict[tuple[int, int], str] = {
    (0x00, 0x42): "Bullet1",
    (0x00, 0x43): "Bullet2",
    (0x00, 0x48): "UXB Green",
    (0x00, 0x49): "UXB Red",
    (0x01, 0x39): "ZzzPop",
    (0x01, 0x3A): "SligToStand / SligTurn",
    (0x01, 0x3B): "SligStep",
    (0x01, 0x3C): "SligSleep1",
    (0x01, 0x3D): "SligSleep2",
    (0x02, 0x3C): "SligShoot",
    (0x02, 0x40): "BulletShell",
    (0x03, 0x39): "MudRoll",
    (0x03, 0x3A): "MudRunSlide",
    (0x03, 0x3B): "LandingSoft",
    (0x03, 0x43): "Sneak",
    (0x03, 0x48): "Knocback",
    (0x04, 0x24): "Footstep1",
    (0x04, 0x25): "Footstep2",
    (0x04, 0x26): "Footstep3",
    (0x04, 0x48): "ElumHitWall",
    (0x05, 0x25): "Scratch",
    (0x05, 0x3D): "ElumHowl",
    (0x05, 0x3F): "SpottedHoney",
    (0x05, 0x40): "ElumEatingHoney1",
    (0x05, 0x41): "ElumEatingHoney2",
    (0x05, 0x42): "ElumEatingHoney3",
    (0x05, 0x43): "ElumBeesStruggle",
    (0x06, 0x24): "Monk",
    (0x06, 0x30): "HandstoneTransition",
    (0x06, 0x35): "RingBellHammer",
    (0x06, 0x3C): "SwitchBellHammer",
    (0x07, 0x23): "Explosion",
    (0x07, 0x3B): "Bees1",
    (0x07, 0x3C): "Bees2",
    (0x07, 0x40): "DovesFlying",
    (0x08, 0x39): "WellEnter",
    (0x08, 0x3A): "WellExit",
    (0x08, 0x3C): "Respawn",
    (0x08, 0x3D): "HoneyDrip",
    (0x09, 0x24): "RockThrow1 / Leaf",
    (0x09, 0x26): "RockBounceOnMine",
    (0x09, 0x27): "SackHit",
    (0x09, 0x28): "RockBounce",
    (0x09, 0x29): "ParticleBurst",
    (0x09, 0x3C): "PickupItem",
    (0x09, 0x3D): "SackWobble",
    (0x0A, 0x3C): "LiftStop",
    (0x0A, 0x3D): "WheelSqueak",
    (0x0B, 0x3C): "GenericMovement",
    (0x0B, 0x3D): "Hoist / MountElum",
    (0x0B, 0x3E): "MountElumSmackNoise",
    (0x0B, 0x3F): "MountingElum",
    (0x0B, 0x40): "ElumGotMounted",
    (0x0B, 0x41): "AbeMountedElum",
    (0x0B, 0x42): "ElumOkay",
    (0x0C, 0x28): "SlogFastBarking",
    (0x0C, 0x29): "SlogGrowl",
    (0x0C, 0x2A): "SlogAngry",
    (0x0C, 0x2C): "SlogJump",
    (0x0D, 0x3C): "LoudFire",
    (0x0E, 0x3D): "Bat1",
    (0x0E, 0x3E): "Bat2",
    (0x0F, 0x3C): "MeatBounce",
    (0x10, 0x30): "Alarm",
    (0x11, 0x24): "ElectricZap",
    (0x11, 0x25): "ElectricGateLoud",
    (0x11, 0x3B): "BirdPortalSpark",
    (0x12, 0x24): "SlogPanting1",
    (0x12, 0x25): "SlogPanting2",
    (0x12, 0x2E): "SlogDeath",
    (0x12, 0x2F): "SlogSleep1",
    (0x12, 0x30): "SlogSleep2",
    (0x13, 0x30): "Trapdoor",
    (0x14, 0x24): "BellLow",
    (0x14, 0x2B): "BellMedium",
    (0x14, 0x30): "BellHigh",
    (0x16, 0x21): "SlogRun",
    (0x16, 0x25): "SlogScratch",
    (0x16, 0x3D): "SlogSlideTurn",
    (0x18, 0x3E): "SecurityOrbHum",
    (0x19, 0x24): "Zap1",
    (0x19, 0x25): "Zap2",
    (0x1D, 0x30): "ZBallSwoosh",
    (0x1E, 0x3C): "FootSwitchPress",
    (0x1F, 0x3C): "RingRopePull",
    (0x20, 0x3D): "DoorEffect",
    (0x21, 0x24): "BirdPortalOpening",
    (0x22, 0x3C): "FlintLock",
    (0x22, 0x3D): "Fire",
    (0x22, 0x3E): "PostFlint",
    (0x23, 0x24): "RollingBallNoise1",
    (0x23, 0x25): "RollingBallNoise2",
    (0x24, 0x3C): "FallingItemLand",
    (0x25, 0x3C): "ParamiteCMon / ParamiteAttack",
    (0x25, 0x3D): "ParamiteStay",
    (0x25, 0x3E): "ParamiteDoIt",
    (0x25, 0x40): "ParamiteLoudStep",
    (0x25, 0x41): "ParamiteSlightStep",
    (0x25, 0x42): "ParamiteHowdy",
    (0x25, 0x43): "ParamiteClimbingWeb / ParamiteDetectedMeat",
    (0x26, 0x3C): "LeverPull",
    (0x27, 0x3C): "ScrabHowl",
    (0x27, 0x3D): "ScrabDeathHowl",
    (0x27, 0x40): "ScrabHitCollision",
    (0x27, 0x41): "KillEffect",
    (0x27, 0x42): "ScrabShredding",
    (0x27, 0x43): "ScrabWalk",
    (0x27, 0x44): "ScrabYell",
    (0x28, 0x3C): "Eating1",
    (0x28, 0x3D): "Eating2",
    (0x2A, 0x40): "GrenadeBounce",
    (0x2B, 0x24): "Pigeon1",
    (0x2B, 0x25): "Pigeon2",
    (0x2B, 0x26): "Pigeon3",
    (0x2B, 0x27): "Pigeon4",
    (0x2B, 0x28): "Pigeon5",
    (0x2B, 0x29): "Pigeon6",
    (0x2B, 0x2A): "Pigeon7",
    (0x2B, 0x2B): "Pigeon8",
    (0x2B, 0x2C): "Pigeon9",
    (0x2B, 0x2D): "Pigeon10",
    (0x2C, 0x3C): "SlingshotExtend",
    (0x2C, 0x3D): "SlingshotShoot",
    (0x2C, 0x3E): "Clean1",
    (0x2C, 0x3F): "Clean2",
    (0x2E, 0x3C): "LCDScreen",
    (0x30, 0x24): "MeatsawOffscreen",
    (0x30, 0x2A): "MeatsawIdle",
    (0x30, 0x3C): "MeatsawDown",
    (0x30, 0x3E): "MeatsawUp",
    (0x31, 0x3C): "IndustrialNoise",
    (0x31, 0x3D): "Vaporize",
    (0x31, 0x3E): "IndustrialTrigger",
    (0x32, 0x24): "GasStart",
    (0x32, 0x30): "GasLoop",
    (0x32, 0x3C): "Choke",
    (0x3A, 0x3C): "WhistleLow",
    (0x3A, 0x3D): "WhistleHigh",
    (0x3B, 0x3C): "MudHello",
    (0x3B, 0x3D): "MudFollowMe",
    (0x3B, 0x3E): "MudAngry",
    (0x3B, 0x3F): "AbeWait",
    (0x3C, 0x3D): "MudFart",
    (0x3C, 0x3F): "MudLaughSoft",
    (0x3D, 0x37): "MudPassword",
    (0x3D, 0x38): "MudKnockbackOuch",
    (0x3D, 0x39): "MudLaughHard",
    (0x3D, 0x3A): "AbeGoodbye",
    (0x3D, 0x3B): "MudOkay",
    (0x3D, 0x3C): "MudRefuse",
    (0x3D, 0x3D): "MudDunno",
    (0x3D, 0x40): "AbeOops1",
    (0x3D, 0x41): "AbeOops2",
    (0x3E, 0x3C): "SligHi",
    (0x3E, 0x3D): "SligHereBoy",
    (0x3E, 0x3E): "SligGetHim",
    (0x3E, 0x3F): "SligStay",
    (0x3F, 0x25): "SligBullshit",
    (0x3F, 0x26): "SligLookOut",
    (0x3F, 0x3C): "SligBullshit2",
    (0x3F, 0x3D): "SligLaugh",
    (0x40, 0x27): "SligFreeze",
    (0x40, 0x3D): "SligWhat",
    (0x40, 0x3E): "SligHelp",
    (0x40, 0x3F): "SligBlurgh",
    (0x41, 0x3C): "MudDeathDropScream",
    (0x41, 0x40): "MudLandingSoft / MudBeesStruggle",
    (0x43, 0x3C): "GlukkonKillHim1",
    (0x43, 0x3D): "GlukkonKillHim2",
    (0x43, 0x3E): "GlukkonLaugh1",
    (0x43, 0x3F): "GlukkonLaugh2",
}

SOUNDS_MAPPING_AE: dict[tuple[int, int], str] = {
    (0x00, 0x2C): "SecurityDoorDeny",
    (0x00, 0x3F): "SecurityOrb",
    (0x00, 0x40): "GrenadeBounce",
    (0x00, 0x42): "Bullet1 / SligCopter_CollideWithWall1",
    (0x00, 0x43): "Bullet2 / SligCopter_CollideWithWall2",
    (0x00, 0x46): "LCDScreen",
    (0x00, 0x48): "GreenTick",
    (0x00, 0x49): "RedTick",
    (0x00, 0x4A): "FallingItemHit",
    (0x01, 0x24): "Fleech_SleepingInhale",
    (0x01, 0x25): "Fleech_SleepingExhale",
    (0x01, 0x30): "SligCopter_Propeller1",
    (0x01, 0x31): "SligCopter_Propeller2",
    (0x01, 0x32): "SligCopter_Propeller3",
    (0x01, 0x33): "BrewMachineUseStart / CrawlingSligTransformStart",
    (0x01, 0x34): "BrewMachineUseMid",
    (0x01, 0x35): "MenuNavigation",
    (0x01, 0x36): "Slig_Reload1",
    (0x01, 0x37): "Slig_Reload2",
    (0x01, 0x39): "BrewMachineUseEmpty / ZPop",
    (0x01, 0x3A): "MinecarStuck / Slig_StandingTurn / Slig_ToStand",
    (0x01, 0x3B): "Slig_RunningStep / Slig_WalkingStep",
    (0x01, 0x3C): "Slig_Snooze2",
    (0x01, 0x3D): "Slig_Snooze1",
    (0x01, 0x56): "BrewMachineUseEnd",
    (0x02, 0x24): "Zap1",
    (0x02, 0x25): "Zap2",
    (0x02, 0x26): "ElectricZap",
    (0x02, 0x27): "ElectricGateLoud",
    (0x02, 0x31): "BirdPortalSpark",
    (0x02, 0x40): "BulletShell",
    (0x03, 0x24): "Mud_RunningFootstep1 / Mud_WalkingFootstep1",
    (0x03, 0x25): "Mud_RunningFootstep2 / Mud_WalkingFootstep2",
    (0x03, 0x26): "Mud_RunningFootstep3 / Mud_WalkingFootstep3",
    (0x03, 0x30): "Chisel",
    (0x03, 0x39): "Mud_RollingNoise",
    (0x03, 0x3A): "Mud_RunSlide",
    (0x03, 0x3B): "Fleech_LandOnFloor / Glukkon_StepSfx2 / Mud_LandingSoftOrKnockbackMetal / Slog_Landing",
    (0x03, 0x3C): "AbeGenericMovement",
    (0x03, 0x3D): "Mud_DeathNoise",
    (0x03, 0x3E): "Clean1",
    (0x03, 0x3F): "Clean2",
    (0x03, 0x41): "Mud_Unknown4",
    (0x03, 0x43): "Mud_SneakFootstep",
    #(0x03, 0x44): "Mud_Unknown5",
    #(0x03, 0x45): "Mud_Unknown1",
    #(0x03, 0x46): "Mud_Unknown2",
    (0x03, 0x48): "Glukkon_StepSfx3 / Mud_Knockback",
    (0x03, 0x49): "Mud_ElumHitWall",
    (0x04, 0x3A): "MeatBounce",
    (0x04, 0x3B): "Bloop",
    (0x04, 0x3C): "Scrab_Howl / Shrykull1",
    (0x04, 0x3D): "Scrab_DeathHowl",
    (0x04, 0x40): "Scrab_HitCollision",
    (0x04, 0x41): "Fleech_DeathByHeight / Fleech_Dismember / Fleech_LedgeHoist / Fleech_LickTarget / KillEffect",
    (0x04, 0x42): "Scrab_Shredding",
    (0x04, 0x43): "Scrab_Walk",
    (0x04, 0x44): "Scrab_Yell / Shrykull2",
    #(0x04, 0x50): "Mud_Unknown6",
    (0x05, 0x3A): "Eating1",
    (0x05, 0x3B): "Eating2",
    (0x05, 0x3C): "Paramite_CMon_or_Attack",
    (0x05, 0x3D): "Paramite_Stay",
    (0x05, 0x3E): "Paramite_DoIt",
    (0x05, 0x40): "Paramite_LoudStep",
    (0x05, 0x41): "Paramite_SlightStep",
    (0x05, 0x42): "Paramite_ClimbingWeb / Paramite_Howdy",
    (0x05, 0x43): "Paramite_DetectedMeat",
    (0x05, 0x48): "WebDrop1",
    (0x05, 0x49): "WebDrop2",
    (0x06, 0x24): "SpiritLockBreak",
    (0x06, 0x25): "SpiritLockShake",
    (0x06, 0x30): "HandstoneTransition",
    (0x06, 0x31): "Fleech_Burp",
    (0x06, 0x32): "Fleech_Devour / Fleech_PatrolCry / Fleech_Scared / Fleech_WakeUp",
    (0x06, 0x34): "Fleech_Unknown",
    (0x06, 0x36): "Fleech_Digesting",
    (0x06, 0x3C): "SlurgKill / SwitchUnknownTrigger",
    (0x06, 0x3D): "Fleech_CrawlRNG1 / SlurgStop",
    (0x06, 0x3E): "Fleech_CrawlRNG2",
    (0x06, 0x3F): "Fleech_CrawlRNG3",
    (0x06, 0x40): "GreeterKnockback",
    (0x06, 0x43): "GreeterLand",
    (0x07, 0x24): "MenuTransition",
    (0x07, 0x3C): "MinecarMovement",
    (0x07, 0x3D): "MinecarStop",
    #(0x07, 0x40): "AbeDove",
    (0x07, 0x40): "Dove",
    #(0x07, 0x40): "FlyingDove",
    (0x07, 0x48): "WaterStart",
    (0x07, 0x49): "WaterFall",
    (0x07, 0x4A): "WaterEnd",
    (0x08, 0x24): "Glukkon_StepSfx1",
    (0x08, 0x3D): "Glukkon_Commere",
    (0x08, 0x3E): "Glukkon_What",
    (0x08, 0x3F): "Glukkon_AllOYa",
    (0x08, 0x40): "Glukkon_DoIt",
    (0x08, 0x41): "Glukkon_Help",
    (0x08, 0x42): "Glukkon_Hey",
    (0x08, 0x43): "Glukkon_StayHere",
    (0x08, 0x45): "Glukkon_Laugh",
    (0x08, 0x46): "Glukkon_Heh",
    (0x08, 0x47): "Glukkon_KillEm",
    (0x09, 0x24): "Leaf",
    (0x09, 0x25): "AirStream",
    (0x09, 0x26): "RockBounceOnMine",
    (0x09, 0x27): "SackHit",
    (0x09, 0x28): "RockBounce",
    (0x09, 0x29): "ParticleBurst",
    (0x09, 0x39): "WellEnter",
    (0x09, 0x3A): "WellExit",
    (0x09, 0x3C): "PickupItem",
    (0x09, 0x3D): "SackWobble",
    (0x09, 0x3E): "FlyingSligSpawn / GlukkonSpawn / ParamiteSpawn / PossessEffect / ScrabSpawn / ShrykullZap / SligSpawn / SlogSpawn",
    #(0x09, 0x3E): "UnusedSpawn",
    (0x0A, 0x23): "IngameTransition",
    (0x0A, 0x24): "PortalOpening",
    (0x0A, 0x28): "DrillMovement",
    (0x0A, 0x2A): "DrillCollision",
    (0x0A, 0x30): "TrapdoorClose / TrapdoorOpen",
    (0x0A, 0x3B): "FootSwitchPress",
    (0x0A, 0x3C): "LiftStop",
    (0x0A, 0x3D): "WheelSqueak",
    (0x0A, 0x3E): "RingRopePull",
    (0x0A, 0x3F): "LeverPull",
    (0x0A, 0x40): "DoorEffect / NakedSligTransformEnd",
    (0x0A, 0x41): "IndustrialNoise",
    (0x0A, 0x42): "IndustrialTrigger / Vaporize",
    (0x0B, 0x24): "AmbientEffect8",
    (0x0B, 0x25): "AmbientEffect9",
    (0x0B, 0x3C): "FallingItemLand",
    #(0x0B, 0x3E): "Mud_Unknown7",
    #(0x0B, 0x40): "Mud_Unknown10",
    #(0x0B, 0x40): "Mud_Unknown8",
    #(0x0B, 0x41): "Mud_Unknown9",
    #(0x0B, 0x42): "Mud_Unknown11",
    (0x0C, 0x21): "Slog_FastStep / Slog_SlowStep",
    (0x0C, 0x28): "Slog_CautiousWoof / Slog_HungryYip / Slog_IdleWoof",
    (0x0C, 0x29): "Slog_IdleGrrr",
    (0x0C, 0x2A): "Slog_IdleGrrAlt",
    (0x0C, 0x2C): "Slog_Bite / Slog_JumpBite",
    (0x0C, 0x2D): "Slog_AttackGrowl",
    (0x0C, 0x2E): "Slog_DeathWhine",
    (0x0C, 0x2F): "Slog_YawnStart",
    (0x0C, 0x30): "Slog_YawnEnd",
    (0x0C, 0x3D): "Slog_Skid",
    (0x0C, 0x3E): "Slog_Padding",
    (0x0D, 0x3C): "AmbientEffect1",
    (0x12, 0x26): "Gas1",
    (0x12, 0x30): "Gas2",
    (0x12, 0x3C): "Choke",
    (0x13, 0x24): "FlyingSpirit1",
    (0x13, 0x3C): "FlyingSpirit2",
    (0x14, 0x24): "AmbientEffect4",
    (0x14, 0x2B): "AmbientEffect3",
    (0x14, 0x30): "AmbientEffect2",
    (0x17, 0x30): "Abe_Goodbye",
    (0x17, 0x3A): "Abe_FartPuh",
    (0x17, 0x3C): "Abe_AllOYa / Mud_AllOYa",
    #(0x17, 0x3D): "Mud_Unknown12",
    (0x17, 0x3E): "Abe_SadUgh",
    #(0x17, 0x3E): "Mud_Unknown13",
    (0x17, 0x3F): "Abe_Sorry",
    #(0x17, 0x3F): "Mud_Unknown14",
    (0x17, 0x40): "Abe_Sick",
    #(0x17, 0x40): "Mud_Unknown15",
    (0x17, 0x42): "Abe_Work",
    (0x17, 0x44): "Abe_HiAngry",
    (0x17, 0x45): "Abe_HiHappy",
    (0x17, 0x46): "Abe_HiSad",
    (0x17, 0x48): "Abe_NoAngry",
    (0x17, 0x49): "Abe_NoSad",
    (0x18, 0x38): "Abe_Hurt2",
    (0x18, 0x39): "Abe_Laugh",
    (0x18, 0x3A): "Abe_NuhUh",
    (0x18, 0x3B): "Abe_Okay",
    (0x18, 0x3C): "Abe_HelloNeutral",
    (0x18, 0x3D): "Abe_FollowMe",
    (0x18, 0x3E): "Abe_Anger",
    (0x18, 0x3F): "Abe_Wait",
    (0x18, 0x40): "Abe_Hurt1",
    (0x18, 0x41): "Abe_DeathDropScream",
    (0x18, 0x42): "Abe_Fart",
    (0x18, 0x43): "Abe_Giggle",
    (0x19, 0x25): "Slig_LookOut",
    (0x19, 0x26): "SecurityDoorLaugh / Slig_Laugh",
    (0x19, 0x27): "GlukkonSwitchBleh / Slig_Blurgh",
    (0x19, 0x39): "Slig_Freeze",
    (0x19, 0x3A): "Slig_What",
    (0x19, 0x3B): "Slig_Help",
    (0x19, 0x3C): "Slig_Hi",
    (0x19, 0x3D): "Slig_GetHim",
    (0x19, 0x3E): "Slig_HereBoy",
    (0x19, 0x3F): "Slig_Stay",
    (0x19, 0x40): "Slig_GotYa",
    (0x19, 0x41): "Slig_Ouch1",
    (0x19, 0x42): "Slig_Bullshit",
    (0x19, 0x43): "Slig_Bullshit2",
    (0x19, 0x44): "Slig_Ouch2",
    (0x1A, 0x28): "AmbientEffect5",
    (0x1D, 0x30): "AmbientEffect6",
    (0x1D, 0x31): "AmbientEffect7",
    (0x22, 0x3D): "Fire",
    (0x27, 0x3C): "SligCopter_ThrowGrenade / SligShoot",
    (0x30, 0x24): "FallingItemPresence1",
    (0x30, 0x2A): "FallingItemPresence2",
    (0x41, 0x40): "Mud_ExhaustingHoistNoise"
}