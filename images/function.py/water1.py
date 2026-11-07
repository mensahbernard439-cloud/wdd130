
#Water Column Height formula
def water_column_height(tower_height, tank_height):

  height = tower_height + 3*tank_height/4 


#Pressure gain from height formula
def pressure_gain_from_water_height(height):

  pressure_gain =pressure*gravity*height/1000


#pressure_loss_from_pipe formula
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

  pressure_l_p =(-friction_factor)*pipe_length*density*fluid_velocity**2


#Pressure loss from fittings

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

  pressure_l_f = (-0.04)*density*velocity**2*quantity_fittings/ 2000


#Reynolds Number

def reynolds_number(hydraulic_diameter, fluid_velocity):

  reynolds_number = density*hydraulic_diameter*fluid_velocity/ dynamic_viscosity


#Pressure loss from pipe reduction

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)

  konst = (0.1+(50/reynolds_number))*((larger_diameter/smaller_diameter)**4-1)

  lost_pressure = (-konst)*density*fluid_velocity**2/2000