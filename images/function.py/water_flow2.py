EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


# Water Column Height formula
def water_column_height(tower_height, tank_height):

    height_water = tower_height + (3 * tank_height) / 4
    return height_water


# Pressure gain from height formula
def pressure_gain_from_water_height(height):

    pressure_gain = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
    return pressure_gain


# Pressure loss from pipe formula
def pressure_loss_from_pipe(
    pipe_diameter, pipe_length, friction_factor, fluid_velocity
):

    pressure_l_p = (
        -friction_factor
        * (pipe_length / pipe_diameter)
        * WATER_DENSITY
        * (fluid_velocity ** 2)
        / 2000
    )
    return pressure_l_p


# Pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

    pressure_l_f = (
        -0.04
        * quantity_fittings
        * WATER_DENSITY
        * (fluid_velocity ** 2)
        / 2000
    )
    return pressure_l_f


# Reynolds number formula
def reynolds_number(hydraulic_diameter, fluid_velocity):

    reynolds = (
        WATER_DENSITY
        * hydraulic_diameter
        * fluid_velocity
        / WATER_DYNAMIC_VISCOSITY
    )
    return reynolds


# Pressure loss from pipe reduction formula
def pressure_loss_from_pipe_reduction(
    larger_diameter, smaller_diameter, fluid_velocity, reynolds_number
):

    if reynolds_number == 0:
        return 0.0

    k = (
        0.1
        + (50 / reynolds_number)
        * ((larger_diameter / smaller_diameter) ** 4 - 1)
    )

    pressure_loss = (
        -k
        * WATER_DENSITY
        * (fluid_velocity ** 2)
        / 2000
    )

    return pressure_loss


def main():
    print("Water Pressure Calculation System")
    print("---------------------------------")

    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank (meters): "))
    pipe_length = float(input("Length of pipe (meters): "))
    quantity_fittings = int(input("Number of fittings: "))
    smaller_diameter = float(input("Smaller pipe diameter (meters): "))

    # Standard values
    pipe_diameter = 0.048692
    friction_factor = 0.018
    fluid_velocity = 1.75
    larger_diameter = 0.286870

    # Water column height
    height = water_column_height(tower_height, tank_height)

    # Pressure gained from water height
    pressure = pressure_gain_from_water_height(height)

    # Pressure loss from pipe
    loss_pipe = pressure_loss_from_pipe(
        pipe_diameter,
        pipe_length,
        friction_factor,
        fluid_velocity
    )
    pressure += loss_pipe

    # Pressure loss from fittings
    loss_fittings = pressure_loss_from_fittings(
        fluid_velocity,
        quantity_fittings
    )
    pressure += loss_fittings

    # Reynolds number
    reynolds = reynolds_number(
        pipe_diameter,
        fluid_velocity
    )

    # Pressure loss from pipe reduction
    loss_reduction = pressure_loss_from_pipe_reduction(
        larger_diameter,
        smaller_diameter,
        fluid_velocity,
        reynolds
    )
    pressure += loss_reduction

    print(f"\nTotal Water Pressure at Outlet: {pressure:.3f} kPa")


if __name__ == "__main__":
    main()