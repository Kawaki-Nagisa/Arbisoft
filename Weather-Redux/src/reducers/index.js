import { FETCH_COORDINATES_ERROR,FETCH_COORDINATES_SUCCESS,FETCH_WEATHER_ERROR,FETCH_WEATHER_SUCCESS } from "../utils/constants";

const initialState = {
    weatherData: [],
    stateCoordinates:[],
  };
  
  const rootReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_COORDINATES_SUCCESS:
        return Object.assign({}, state, {
          stateCoordinates: state.stateCoordinates.concat(action.payload)
      })
        //return { ...state, coordinates: action.payload, error: null };
      case FETCH_WEATHER_SUCCESS:  
      return Object.assign({}, state, {
          weatherData: state.weatherData.concat(action.payload)
      })
        //return { ...state, weatherData: action.payload, error: null };
      case FETCH_COORDINATES_ERROR:
      case FETCH_WEATHER_ERROR:
        return { ...state, error: action.payload };  
      default:
        return state;
    }
  };
  
  export default rootReducer;
  