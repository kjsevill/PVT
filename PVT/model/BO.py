def Bo(colums,Rs, Yg, Yo, T ):
    """"
    Parameters
    ---------------
    colums:
        Correlación usada
    Rs:
        Solubilidad del gas en PCN/BN
    Yg:
        Gravedad específica del gas en solución
    Yo:
        Gravedad específica del crudo en superficie
    T:
        Temperatura del sistema en °R
    Returns
        float number  -> Bo
    """
    a=0.742300
    b=0.323200
    c=-1.2020
    F = (Rs**a) * (Yg**b) * (Yo**c)

    if colums == "Standing":
        Bo = 0.9759 + 0.00012*(Rs*((Yg/Yo)^0.5) + 1.25*(T-460))^(1.2)
    else:
        Bo = 0.497069 + 0.862963 * (10**(-3)) * T + 0.182594 * 10**(-2) * F + 0.318099 * 10**(-5) * F**(2)

    return Bo

