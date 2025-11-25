#usando o video https://www.youtube.com/watch?v=pn_-2e0-6iE&list=RDpn_-2e0-6iE&start_radio=1
#baixei em mp3 e vou cortar em 7 notas para a reprodução do som 
import subprocess
timestamps = [
    
    "0:09",
    "0:18",
    "0:27",
    "0:36",
    "0:45",
    "0:54",
    "1:03"
]

input_file = r"C:\usp\labdigII\projeto\notas\trombone.mp3"

def to_seconds(t):
    m, s = t.split(":")
    return int(m) * 60 + int(s)

starts = [to_seconds(t) for t in timestamps]
for i in range(len(starts)):
    start = starts[i]

    if i < len(starts) - 1:
        end = starts[i+1]
        duration = 1
    else:
        duration = None
    
    output_file = fr"C:\usp\labdigII\projeto\notas\{i+1}.mp3"

    cmd = ["ffmpeg", "-y", "-i", input_file, "-ss", str(start)]

    if duration is not None:
        cmd += ["-t", str(duration)]

    cmd += ["-c", "copy", output_file]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd)
