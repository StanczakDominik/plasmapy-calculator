from application import app
from flask import Flask, render_template, request
import plasmapy
import astropy
import astropy.units as u
import plasmapy.formulary.parameters as pfp

# Thermal Pressure


def calculate_thermal_pressure(form):
    num1 = form['temp']
    num2 = form['density']

    unit1 = u.Unit(form['unitsT'])
    q1 = u.Quantity(num1, unit1)
    unit2 = u.Unit(form['unitsN'])
    q2 = u.Quantity(num2, unit2)
    sum = pfp.thermal_pressure(q1, q2)
    return sum

# Debye length


def calculate_debye_length(form):
    num1 = form['temp']
    num2 = form['density']

    unit1 = u.Unit(form['unitsT'])
    q1 = u.Quantity(num1, unit1)
    unit2 = u.Unit(form['unitsN'])
    q2 = u.Quantity(num2, unit2)
    sum = pfp.Debye_length(q1, q2)
    return sum

# Gyrofrequency


def calculate_gyrofrequency(form):
    mag_fld = form['mf_mag']
    mag_unit = form['unitsB']
    particle = form['particle']
    z = form['z']
    signed = form['signed']
    to_hz = form['to_hz']

    if mag_fld == None or mag_unit == 'select':
        return render_template('gyrofrequency.html', sum="Enter all required fields")

    # Gyrofrequency with only Magnetic Field and Particle
    b = u.Quantity(mag_fld, u.Unit(mag_unit))
    p = plasmapy.particles.Particle(particle)
    sum = pfp.gyrofrequency(b, p)

    # Gyrofrequency with B, particle, z

    # Gyrofrequency with B, particle, z, signed

    # Output if to_hz is true
    return sum


# Inertial length


def calculate_inertial_length(form):
    n = form['n']
    p = form['particle']

    n_quantity = u.Quantity(n, u.Unit(form['unitsN']))
    sum = pfp.inertial_length(n_quantity, p)
    return sum
