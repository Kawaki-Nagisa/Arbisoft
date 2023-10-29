import { FETCH_COORDINATES_ERROR,FETCH_COORDINATES_SUCCESS,FETCH_WEATHER_ERROR,FETCH_WEATHER_SUCCESS } from "../utils/constants";
import { getCoordinatesByState, getWeatherDataByCoordinates } from "../utils/api";

export const fetchCoordinates = (state) => {
  return async (dispatch) => {
    try {
      const coordinates = await getCoordinatesByState(state);
      dispatch({ type: FETCH_COORDINATES_SUCCESS, payload: coordinates });
    } catch (error) {
      dispatch({ type: FETCH_COORDINATES_ERROR, payload: error });
    }
  };
};

export const fetchWeatherData = (lat, lon) => {
  return async (dispatch) => {
    try {
      const weatherData = await getWeatherDataByCoordinates(lat, lon);
      dispatch({ type: FETCH_WEATHER_SUCCESS, payload: weatherData });
    } catch (error) {
      dispatch({ type: FETCH_WEATHER_ERROR, payload: error });
    }
  };
};
