from librosa import note_to_hz,load,feature,yin
import numpy as np
import warnings
import soundfile as sf
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    def pitch_to_frequency(pitch):
        return 16.35*(2.0**(float(pitch)/12.0))
    def note_frequency(note):
        return note_to_hz(note)
    def get_avg_spectral_centroid(file):
        y,sr=load(file)
        centroid=feature.spectral_centroid(y=y,sr=sr)
        return np.average(centroid.T)
    def fundamental_frequency(file,target_freq,dif_threshold=90):
        y,srate=load(file)
        Y=yin(y,65,2093,sr=srate)
        adj_avg=[]
        for elem in np.nditer(Y):
            if np.abs(elem-target_freq)<dif_threshold:
                adj_avg.append(float(elem))
        return np.average(np.array(adj_avg))
    #print(FundamentalFrequency('a5_open_test.wav',880))
            
    def get_pick_attack_len(wave):
        w,sr=sf.read(wave)
        peakIndex=0
        biggest=0
        for idx,val in enumerate(np.nditer(w)):
            if np.abs(val)>biggest:
                biggest=np.abs(val)
                peakIndex=idx
        return float(peakIndex)/float(sr)
