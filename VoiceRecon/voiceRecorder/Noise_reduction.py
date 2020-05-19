from VoiceRecon.voiceRecorder import pyfil as pf

# Z = pf.Voice2Data('Alarm01.wav')
filename = ('C:/Desarrollo/Voice-Recon/VoiceRecon/media/record.wav')
X = pf.Voice2Data(filename)
print(len(X))
