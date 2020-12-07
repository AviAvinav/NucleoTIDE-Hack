import eel
import chempy
from chempy import balance_stoichiometry
from math import *
from chempy import Substance

eel.init('web2')

#Function that recieves the input of the mass of the compound and divides by inputted molarMass to get mols
@eel.expose
def mol_conv(material_mass, molar_mass):
  num_mole = ((material_mass)/(molar_mass))
  return num_mole

#Function that takes the input of the number of atoms and uses avogadro's number to find moles
@eel.expose
def mols_avogadros_num(material_atoms):
  avogadro_num = 6.022 * (10 ** 23)
  num_mole = (material_atoms / avogadro_num)
  return num_mole

@eel.expose
def mols_given_volume(volume):
  molar_volume = 22.4
  num_mole = (volume / molar_volume)
  return num_mole

#Functon that takes the inputs of mols and volume to calculate the concentration
@eel.expose
def conc_mols_vol(num_mole, volume):
  conc = num_mole/volume
  return conc

#Function that finds the concentration using the material mass, molar mass and total volume
@eel.expose
def concentration(material_mass, molar_mass, tot_volume):
  concentration = (material_mass/molar_mass) * tot_volume
  return concentration

#Function that determines the rate of reaction using the change in products/reactants and time
@eel.expose
def rate_of_reaction(delta_products_reactants, delta_time):
  rate = delta_products_reactants/delta_time
  return rate

#This is a function that determines the rate of reaction using mass and time
@eel.expose
def rate_of_reaction_mass(delta_mass, delta_time):
  rate = delta_mass/delta_time
  return rate

#Function that finds the rate of reaction with volume
@eel.expose
def rate_of_reaction_vol(delta_volume, delta_time):
  rate = delta_volume/delta_time
  return rate

#Function that finds the percent composition of one element inside the entire compound
@eel.expose
def percent_composition(element_mass, total_mass):
  percentage = element_mass/total_mass
  return percentage
  
eel.start('index.html')