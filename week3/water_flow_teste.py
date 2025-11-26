def water_column_height(tower_height, tank_height):

    h = tower_height + (3 * tank_height) / 4
    return h


def pressure_gain_from_water_height(height):

    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    
    # P = ρgh / 1000 (to convert from Pa to kPa)
    pressure = (density * gravity * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    density = 998.2  # kg/m^3
    
    # P = -f * L * ρ * v² / (2000 * d)
    pressure_loss = (-friction_factor * pipe_length * density * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

    density = 998.2  # kg/m^3
    
    # P = -0.04 * ρ * v² * n / 2000
    pressure_loss = (-0.04 * density * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss


def reynolds_number(hydraulic_diameter, fluid_velocity):

    density = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016  # Pa·s
    
    # R = ρ * d * v / μ
    reynolds = (density * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):

    density = 998.2  # kg/m^3
    
    # k = 0.1 + (50 / R) * ((D/d)^4 - 1)
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    
    # P = -k * ρ * v² / 2000
    pressure_loss = (-k * density * fluid_velocity**2) / 2000
    return pressure_loss