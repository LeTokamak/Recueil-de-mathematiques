import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

x = np.linspace(-2*np.pi, 2*np.pi, 10_000)

cm = 1/2.54

def rien(x):
    return x

def tracer_couple_fct(fct_1, fct_2, 
                      label_1, label_2, 
                      color_1, color_2,
                      y_lim_1, y_lim_2,
                      x_lim_1, x_lim_2,
                      liste_ticks_x, liste_ticks_y,
                      label_ticks_x, label_ticks_y,
                      titre, nom):

    fig, ax_trigo = plt.subplots(figsize=(29.7*cm*1/1.25, 21*cm*1/1.25))
    ax_normal = ax_trigo.twinx()

    # automatically update ylim of ax2 when ylim of ax1 changes.
    ax_trigo.callbacks.connect("ylim_changed", rien)
    ax_trigo.plot(np.linspace(-40, 120, 100))
    ax_trigo.set_xlim(0, 100)

    ax_trigo.set_title('Two scales: Fahrenheit and Celsius')
    ax_trigo.set_ylabel('Fahrenheit')
    ax_normal.set_ylabel('Celsius')


    plt.figure() # Format A4
    
    fig.plot(x, fct_1(x), color=color_1, label=label_1)
    fig.plot(x, fct_2(x), color=color_2, label=label_2)
    fig.legend()
    
    fig.ylim(y_lim_1, y_lim_2)
    fig.xlim(x_lim_1, x_lim_2)
    
    fig.xticks(liste_ticks_x, label_ticks_x)
    fig.yticks(liste_ticks_y, label_ticks_y)
    
    # Ajouter des titres et des labels
    fig.title(titre)
    fig.xlabel(r'$\theta$')
    
    # Enregistrer le graphique
    fig.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Graphs fonctions/{nom}.png', dpi=300)
    
tracer_couple_fct(np.sin, np.cos,
                  r'$\sin(\theta)$', r'$\cos(\theta)$',
                  'blue', 'red',
                  -1.1, 1.1,
                  -np.pi, np.pi,
                  [-np.pi, -5*np.pi/6, -3*np.pi/4, -2*np.pi/3, -np.pi/2, -np.pi/3, -np.pi/4, -np.pi/6, 0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi],
                  [-1, -((3)**0.5)/2, -((2)**0.5)/2, -0.5, 0, 0.5, ((2)**0.5)/2, ((3)**0.5)/2, 1],
                  [r'$\frac{~}{~}\pi$', r'$\frac{~}{~}\frac{5\pi}{6}$', r'$\frac{~}{~}\frac{3\pi}{4}$', r'$\frac{~}{~}\frac{2\pi}{3}$', r'$\frac{~}{~}\frac{\pi}{2}$', r'$\frac{~}{~}\frac{\pi}{3}$', r'$\frac{~}{~}\frac{\pi}{4}$', r'$\frac{~}{~}\frac{\pi}{6}$', r'$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$', r'$\pi$'],
                  [r"$-1$", r"$-\frac{\sqrt{3}}{2}$", r"$-\frac{\sqrt{2}}{2}$", r"$-\frac{1}{2}$", r"$0$", r"$\frac{1}{2}$", r"$\frac{\sqrt{2}}{2}$", r"$\frac{\sqrt{3}}{2}$", r"$1$"],
                  'Graphique des fonctions sinus et cosinus', 'sinus_cosinus')