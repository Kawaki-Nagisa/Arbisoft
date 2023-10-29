import axios from "axios";

const baseURL = "http://api.openweathermap.org";
const apiKey = "77f0546781a3c7106da4a9477dbe28c9";

const instance = axios.create({
  baseURL,
});

export const getCoordinatesByState = async (state) => {
  try {
    const response = await instance.get(
      `/geo/1.0/direct?q=${state},US&limit=1&appid=${apiKey}`
    );


    return {
      State: response.data[0].name,
      Lat: response.data[0].lat,
      Lon: response.data[0].lon,
    };
  } catch (error) {
    throw error;
  }
};

export const getWeatherDataByCoordinates = async (lat, lon) => {
  try {
    const response = await instance.get(
      `/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${apiKey}`
    );

    const selectedData = response.data.list.slice(0, 5).map((item) => ({
      temperature: item.main.temp,
      pressure: item.main.pressure,
      humidity: item.main.humidity,
    }));

    return [selectedData];
  } catch (error) {
    throw error;
  }
};

