
import numpy as np
import scipy.signal as signal

def filtro(omega_p, omega_r, numtaps=201):
    """
    Gera um filtro FIR passa-baixas usando janela de Hamming.
    
    Parâmetros:
    -----------
    omega_p : float
        Frequência de passagem (normalizada por Nyquist, entre 0 e 0.5).
    omega_r : float
        Frequência de rejeição (normalizada por Nyquist, entre 0 e 0.5).
    numtaps : int
        Número de coeficientes (quanto maior, melhor a rejeição, mas maior o custo)
    
    Retorna:
    --------
    h : array
        Coeficientes do filtro FIR
    """
    cutoff = (omega_p + omega_r) / 2
    h = signal.firwin(numtaps, cutoff, window="hamming")
    return h
