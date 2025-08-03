# test_module.py

import unittest
import matplotlib
matplotlib.use('Agg')
import time_series_visualizer

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df_clean['value'].mean())
        expected = 20512
        self.assertEqual(actual, expected, "Expected dataframe cleaned average incorrect.")


class LinePlotTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertEqual(fig.get_axes()[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


class BarPlotTestCase(unittest.TestCase):
    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertEqual(fig.get_axes()[0].get_xlabel(), "Years")
        self.assertEqual(fig.get_axes()[0].get_ylabel(), "Average Page Views")


class BoxPlotTestCase(unittest.TestCase):
    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertEqual(fig.get_axes()[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(fig.get_axes()[1].get_title(), "Month-wise Box Plot (Seasonality)")

if __name__ == "__main__":
    unittest.main()
