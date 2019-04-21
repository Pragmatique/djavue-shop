import { HTTP2 } from './common'

export const User = {
  create (config) {
    console.log(config)
    return HTTP2.post('/users/', config).then(response => {
      return response.data
    })
  },
  delete (user) {
    return HTTP.delete(`/users/${user.id}/`)
  },
  update (config) {
    console.log(config)
    return HTTP2.post(`/user/${user.id}/`, config).then(response => {
      return response.data
    })
  }

}
