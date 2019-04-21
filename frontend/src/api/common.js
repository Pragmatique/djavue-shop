import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/v1/'
})

export const HTTP2 = axios.create({
  baseURL: 'http://localhost:8000/api/auth/'
})
