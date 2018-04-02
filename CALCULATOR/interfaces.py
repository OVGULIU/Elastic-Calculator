#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Graphical elements
"""
from __future__ import division, print_function
from os import sys
sys.path.append('../CALCULATOR/')
from sympy import init_printing
init_printing()


def mesh_gui():
    try:
        import easygui
        msg = "General Discretization Parameters"
        title = "Mesh parameters"
        fieldNames = ["Element size","Element type (2: lin.triang.; 3 quad4; 9.quad.triang.)","Interpolation order"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        c = float(fieldValues[0])
        ietype = int(fieldValues[1])
        order = int(fieldValues[2])
    except:
        c1 = raw_input("Element size")
        ietype1 = raw_input("Element type")
        order1 = raw_input("Interpolation order")
        c = float(c1)
        ietype = int(ietype1)
        order = int(order1)

    return c, ietype , order

def ring_prs():
    try:
        import easygui
        msg = "Cylinder under internal pressure"
        title = "Problem parameters"
        fieldNames = ["Internal radius","External radius","Internal pressure","External pressure"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        a = float(fieldValues[0])
        b = float(fieldValues[1])
        pa = float(fieldValues[2])
        pb = float(fieldValues[3])
    except:
        a1 = raw_input("Internal radius")
        b1 = raw_input("Eternal radius")
        c1 = raw_input("Internal pressure")
        d1 = raw_input("xternal pressure")
        a  = float(a1)
        b  = float(b1)
        pa = float(c1)
        pb = float(d1)

    return a , b , pa , pb

def ring_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Cylinder under internal and external pressure",
        ok_button="Continuar",
        image='anillo.gif')
    except:
        print ("No easygui module")

    return



def wedge_prs():


    try:
        import easygui
        msg = "Self equilibrated wedge"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length", "Poissons ratio" , "Youngs modulus" , "External shear"]
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        phid = float(fieldValues[0])
        l = float(fieldValues[1])
        enu = float(fieldValues[2])
        emod = float(fieldValues[3])
        S = float(fieldValues[4])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Poissons ratio")
        d1 =raw_input("Youngs modulus")
        e1 = raw_input("External shear")
        phid = float(a1)
        l = float(b1)
        enu = float(c1)
        emod = float(d1)
        S = float(e1)

    return phid , l , enu , emod , S

def wedge_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Self-equilibrated wedge",
        ok_button="Continuar",
        image='cunia.gif')
    except:
        print ("No easygui module")

    return

def beam_prs():

    try:
        import easygui
        msg = "Cantilever beam (Timoshenko Sln)"
        title = "Enter the problem parameters"
        fieldNames = ["Length","Height","Inertia","Poissons ratio","Young modulus", "Load"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        L  = float(fieldValues[0])
        h  = float(fieldValues[1])
        I  = float(fieldValues[2])
        nu = float(fieldValues[3])
        E  = float(fieldValues[4])
        P  = float(fieldValues[5])
    except:
        a1 = raw_input("Length")
        b1 = raw_input("Height")
        c1 = raw_input("Inertia")
        d1 = raw_input("Poissons ratio")
        e1 = raw_input("Youngs modulus")
        f1 = raw_input("Load")
        L = float(a1)
        h = float(b1)
        I = float(c1)
        nu = float(d1)
        E = float(e1)
        P = float(f1)

    return L , h , I , nu , E , P

def quad_prs():

    try:
        import easygui
        msg = "Square Box"
        title = "Enter the problem parameters"
        fieldNames = ["Length" , "Height" , "Angle of incidence" , "Wave propagation velocity" , "Total time" , "Central time" , "Central frequency" ]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg , title , fieldNames)


        L     = float(fieldValues[0])
        h     = float(fieldValues[1])
        gamma = float(fieldValues[2])
        beta  = float(fieldValues[3])
        Tt    = float(fieldValues[4])
        Tc    = float(fieldValues[5])
        fc    = float(fieldValues[6])


    except:
        a1 = raw_input("Length")
        b1 = raw_input("Height")
        d1 = raw_input("Angle of incidence")
        e1 = raw_input("Wave velocity")
        f1 = raw_input("Total time")
        g1 = raw_input("Central time")
        h1 = raw_input("Central frequency")
        L = float(a1)
        h = float(b1)
        gamma = float(d1)
        beta = float(e1)
        Tt = float(f1)
        Tc = float(g1)
        fc = float(h1)

    return L , h , gamma , beta , Tt , Tc , fc

def membrane_prs():

    try:
        import easygui
        msg = "Square Box"
        title = "Enter the problem parameters"
        fieldNames = ["b" , "a" , "Material velocity" , "Number of increments" , "Total time"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg , title , fieldNames)


        L     = float(fieldValues[0])
        h     = float(fieldValues[1])
        beta  = float(fieldValues[2])
        ninc  = int(fieldValues[3])
        Tt    = float(fieldValues[4])


    except:
        a1 = raw_input("b")
        b1 = raw_input("a")
        d1 = raw_input("Beta")
        c1 = raw_input("Total increments")
        f1 = raw_input("Total time")
        L = float(a1)
        h = float(b1)
        beta = float(d1)
        ninc = int(c1)
        Tt = float(f1)

    return L , h , beta , ninc , Tt

def modal_prs():

    try:
        import easygui
        msg = "Square Box"
        title = "Enter the problem parameters"
        fieldNames = ["b" , "a" , "Material velocity" , "x-mode" , "y-mode" , "Number of increments" , "Total time"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg , title , fieldNames)


        L     = float(fieldValues[0])
        h     = float(fieldValues[1])
        beta  = float(fieldValues[2])
        m  = int(fieldValues[3])
        n  = int(fieldValues[4])
        ninc  = int(fieldValues[5])
        Tt    = float(fieldValues[6])


    except:
        a1 = raw_input("b")
        b1 = raw_input("a")
        d1 = raw_input("Beta")
        e1 = raw_input("x-mode m")
        h1 = raw_input("y-mode n")
        c1 = raw_input("Total increments")
        f1 = raw_input("Total time")
        L = float(a1)
        h = float(b1)
        beta = float(d1)
        m = int(e1)
        n = int(h1)
        ninc = int(c1)
        Tt = float(f1)

    return L , h , beta , m , n , ninc , Tt



def beam_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Cantilever beam under point load (Timoshnko sln)",
        ok_button="Continuar",
        image='viga.gif')
    except:
        print ("No easygui module")

    return


def boussi_prs():
    try:
        import easygui
        msg = "Half-space under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Length","Height","Point load","Poissons ratio","Youngs modulus"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        l  = float(fieldValues[0])
        h  = float(fieldValues[1])
        P  = float(fieldValues[2])
        nu = float(fieldValues[3])
        E  = float(fieldValues[4])
    except:
        a1 = raw_input("Length")
        b1 = raw_input("Height")
        c1 = raw_input("Point load")
        d1 = raw_input("Poissons ratio")
        e1 = raw_input("Youngs modulus")
        l  = float(a1)
        h  = float(b1)
        P  = float(c1)
        nu = float(d1)
        E  = float(e1)

    return l, h , P, nu , E

def boussi_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Half-space under point loads",
        ok_button="Continuar",
        image='boussi.gif')
    except:
        print ("No easygui module")

    return


def flamantP_prs():

    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Point load"]
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Point load")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)


    return phid , l , P

def flamantp_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under point load (Flamant sln)",
        ok_button="Continuar",
        image='flamantP.gif')
    except:
        print ("No easygui module")

    return



def flamantM_prs():

    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Applied moment"]
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Applied moment")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)


    return phid , l , P

def flamantM_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under point moment (Flamant sln)",
        ok_button="Continuar",
        image='flamantM.gif')
    except:
        print ("No easygui module")

    return



def flamantQ_prs():

    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Point load"]
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Point load")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)


    return phid , l , P

def flamantQ_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under transverse load (Flamant sln)",
        ok_button="Continuar",
        image='flamantQ.gif')
    except:
        print ("No easygui module")

    return



def canyon_prs():
    try:
        import easygui
        msg = "Semi-circular canyon under SH waves"
        title = "Enter the problem parameters"
        fieldNames = ["Radius (1.0)","Side length(10.0)","Height (10.0)","Number of increments (4097)" , "Angle of incidence (in rads)"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)


        r = float(fieldValues[0])
        l = float(fieldValues[1])
        h = float(fieldValues[2])
        Ninc = int(fieldValues[3])
        gamma = float(fieldValues[4])
    except:
        a1 = raw_input("Radius")
        b1 = raw_input("Side length")
        c1 = raw_input("Hight")
        d1 = raw_input("Number of increments")
        e1 = raw_input("Angle of incidence (in rads)")
        r = float(a1)
        l = float(b1)
        h = float(c1)
        Ninc = int(d1)
        gamma= float(e1)

    return r , l , h , Ninc , gamma

def canion_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Semi-circular canyon under incident SH waves (TRifunac sln)",
        ok_button="Continuar",
        image='canion.gif')
    except:
        print ("No easygui module")

    return

def dam_prs():
    try:
        import easygui
        msg = "45 degree dam under hydrostatic pressure"
        title = "Problem parameters"
        fieldNames = ["Height"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        H = float(fieldValues[0])
    except:
        a1 = raw_input("Height")
        H  = float(a1)
        print ("No easygui module")

    return H

def dam_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="45 degree dam under hydrostatic pressure",
        ok_button="Continuar",
        image='dam.gif')
    except:
        print ("No easygui module")

    return

def box_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Rectangular domain for wave propagation analysis",
        ok_button="Continuar",
        image='box.gif')
    except:
        print ("No easygui module")

    return

def ellipse_hlp():
    
    try:
        import easygui
        easygui.msgbox(msg="Seccion transversal eliptica de un eje sometido a torsion pura.",
        title="Elipse", 
        ok_button="Continuar",
        image='ellipse.gif')
    except:
        print ("No easygui module")
    
    return
def ellipse():
    
    try:
        import easygui
        msg = "Ingrese los parametros del problema"
        title = "Elipse"
        fieldNames = ["a" , "b","Tamaño del elemento","Tipo de elemento","Orden","Contornos"]
        fieldValues = []  ## se empieza con espacios blancos
        fieldValues = easygui.multenterbox(msg , title , fieldNames)
        
    
        a     = float(fieldValues[0])
        b     = float(fieldValues[1])
        c  = float(fieldValues[2]) 
        ietype  = int(fieldValues[3])
        order = int(fieldValues[4])
        contornos = int(fieldValues[5])
    except:
        a1 = raw_input("a")
        b1 = raw_input("b")
        d1 = raw_input("Tamaño del elemento")
        c1 = raw_input("Tipo de elemento")
        e1= raw_input("Orden")
        f1= raw_input("Contornos")
        a = float(a1)
        b = float(b1)
        c = float(d1)
        ietype = int(c1)
        order=int(e1)
        order=int(f1)
            
    return a , b , c , ietype , order, contornos

