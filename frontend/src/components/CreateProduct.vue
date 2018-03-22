<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    header.text-center
      h2 Please, make your purchase
    .form-group
      .col-3
        label.form-label Name
      .col-9
        input.form-input(type="text" v-model="name" placeholder="Type product name...")
    .form-group
      .col-3
        label.form-label Description
      .col-9
        input.form-input(type="text" v-model="description" placeholder="Type product description...")
    .form-group
      .col-3
        label.form-label Price
      .col-9
        input.form-input(type="number" v-model="price" placeholder="Input product price...")
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Create
</template>

<script>
export default {
  name: 'create-product',
  data () {
    return {
      'name': '',
      'description': '',
      'price': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createProduct()

      this.name = ''
      this.description = ''
      this.price = ''

      event.preventDefault()
    },
    createProduct () {
      this.$store.dispatch('createProduct', { name: this.name, description: this.description, price: this.price })
      console.log({ name: this.name, description: this.description, price: this.price })
    }
  }
}
</script>

<style>
</style>
