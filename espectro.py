import numpy as np
import matplotlib.pyplot as plt

def espectro(x, Fs, titulo="Espectro"):
    """
    Plota o espectro de magnitude de um sinal x[n].
    
    Parâmetros:
    -----------
    x : array
        Sinal de entrada
    Fs : int
        Frequência de amostragem (Hz)
    titulo : str
        Título do gráfico
    """
    N = 8192  # tamanho da FFT
    X = np.fft.fftshift(np.fft.fft(x, N))
    freqs = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))

    plt.figure(figsize=(10,4))
    plt.plot(freqs, 20*np.log10(np.abs(X)+1e-6))
    plt.title(titulo)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
