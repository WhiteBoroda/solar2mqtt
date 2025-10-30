Import("env")

env.Append(CPPDEFINES=[
    ("SWVERSION", env.StringifyMacro(env.GetProjectOption("custom_prog_version"))),
    ("HWBOARD", env.StringifyMacro(env["BOARD"])),
])

if env.GetProjectOption("custom_hardwareserial") == "true":
    env.Append(CPPDEFINES=[
        ("isUART_HARDWARE",  env.StringifyMacro(env.GetBuildType())),
    ])

env.Replace(PROGNAME="Solar2MQTT_%s_%s" % (str(env["BOARD"]), env.GetProjectOption("custom_prog_version")))
