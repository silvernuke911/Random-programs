import numpy as np
import matplotlib.pyplot as plt

space=1000

def circle():
    x_0, y_0 = 0, 0
    r = 1
    t = np.linspace(0,2*np.pi,space+1)
    x = x_0 + r * np.cos(t)
    y = y_0 + r * np.sin(t)

    plt.plot(x,y,color = 'red')
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_axisbelow(True)
    plt.axis('square')
    plt.grid()
    plt.show()

def sphere():
    theta = np.linspace(0, 2*np.pi, space+1)
    phi   = np.linspace(0, np.pi  , space+1)
    radius = 1 

    x_0,y_0,z_0 = 0,0,0
    x = x_0 + radius*np.outer(np.cos(theta),np.sin(phi))
    y = y_0 + radius*np.outer(np.sin(theta),np.sin(phi))
    z = z_0 + radius*np.outer(np.ones(np.size(theta)),np.cos(phi))

    fig = plt.figure()
    ax  = plt.axes(projection = '3d')
    ax.plot_surface(x,y,z)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def spring():
    r = 1
    t = np.linspace(0,2*np.pi,space+1)
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = t

    fig = plt.figure()
    ax  = plt.axes(projection = '3d')
    ax.plot(x,y,z)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def polar():
    t = np.linspace(0,2*np.pi,space+1)
    r = t

    # fig = plt.figure()
    # ax  = plt.axes(projection = 'polar')
    plt.polar(t,r)
    plt.plot()
    plt.show()

def ellipse():
    a = 1
    e = 0.99

    t = np.linspace(0,2*np.pi,space+1)
    r = a*(1-e**2) / (1 + e * np.cos(t))

    plt.polar(t,r)
    plt.show()
ellipse()


