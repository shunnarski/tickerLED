import pandas
import numpy
from scipy.interpolate import interp1d

"""
Gets the interpolated data results of the raw stock/crypto values to construct the graph
based on the number of LED lights available in the grid being used to produce the graph.

Params:

raw_df - The raw values of the stock/crypto values
led_grid_width - The width of the grid based in LED lights available
led_grid_height - The height of the grid based on the LED lights available

"""
def get_interpolated_data_results(raw_df, led_grid_width, led_grid_height):
    pass


def get_interpolated_stock_prices(open_times, open_prices, led_grid_width, led_grid_height):

    start_time, end_time = open_times[0], open_times[-1]
    step = (end_time - start_time) // led_grid_width
    
    interp_times = range(start_time, end_time-step, step)
    kind = 'linear'
    interp_func = interp1d(open_times, open_prices, kind=kind)
    
    interp_values = interp_func(interp_times)

    df_data = {
        'values': interp_values,
        'times': interp_times
    }

    df = pandas.DataFrame(data=df_data)

    df['max'] = max(interp_values)
    df['min'] = min(interp_values)

    return df


