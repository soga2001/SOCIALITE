import axios from 'axios';
import { useCookies } from 'vue3-cookies';

const {cookies} = useCookies();

export const http = axios.create({
  baseURL: `https://localhost:8000/`,
  withCredentials: true,
})

