import math

# --Fixed Parameters perfusion--
# mu (Pa.s)
# p (kg/m3)
# r0 (m)
# Q (m^3/s)
# k_b  (k_b=remains constant since ratio Rb/2*r0 is really high) (no analytical formula)
# g (m/s2)

# --Tuneable Parameter--
# length (length of tubing)
# R_b (bend diamater)
# n (number of turns)

# --Fixed Parameters chip--
# length_chip (length of chip to waste)

# PERFUSION SYSTEM

def velocity(Q, r0):
    # Calculate velocity needed in perfusion (m/s)
    u = Q/(math.pi * r0**2) #mm/s
    return u

def resistance_length(mu, length, r0):
    # Resistance for the length (ohm)
    res_length = (8*mu*length)/(math.pi * r0**4)
    return res_length

def reynolds_number(p, u, r0, mu):
    # Reynolds number
    Rn = (p*u*2*r0)/mu 
    return Rn

def friction_factor(Rn):
    # Friction Factor
    Ff = 64/Rn
    return Ff

def resistance_360(Ff, p, Q, R_b, r0, k_b):
    # Resistance for 360 (ohm)
    res_360 = (0.25*Ff*p)*(Q/math.pi)*(R_b/r0**5)*(360/180) + (0.5*k_b*p)*(Q/(math.pi**2 * r0**4))
    return res_360

def resistance_180(Ff, p, Q, R_b, r0, k_b):
    # Resistance for 180 (ohm)
    res_180 = (0.25*Ff*p)*(Q/math.pi)*(R_b/r0**5)*(180/180) + (0.5*k_b*p)*(Q/(math.pi**2 * r0**4))
    return res_180

def resistance_90(Ff, p, Q, R_b, r0, k_b):
    # Resistance for 90 (ohm)
    res_90 = (0.25*Ff*p)*(Q/math.pi)*(R_b/r0**5)*(90/180) + (0.5*k_b*p)*(Q/(math.pi**2 * r0**4))
    return res_90

def resistance_perfusion(res_length, n, res_360):
    # Total resistance perfusion system (ohm)
    res_perfusion = res_length + n*res_360
    return res_perfusion

def pressure_drop(res_tot, Q):
    # The pressure drop (Pa)
    dP=res_tot*Q
    return dP

def reservoir_height(dP, p, u, g):
    # The height of the reservoir (cm)
    h=100*(dP+0.5*p*u**2)/(p*g)
    return h

def tube_length_coils_optimization(r0, mu, res_360, h, p, g, u, Q, R_b):
    x = 1
    ni = 0
    while ni <= x:
        ni += 1
        L = (math.pi*r0**4/(8*mu))*(-ni*res_360 + ((h*p*g)-(0.5*p*u**2))/Q)
        x = (L-0.10)/(2*math.pi*R_b)
        x = round(x)
    return L, x