<template lang="pug">
  #app
    header.text-center
      h2 List of products in your basket
    .card(v-for="product in products")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteProduct(product)")
        .card-title {{ product.name }}
        .card-subtitle {{ product.price }}
      .card-body {{ product.description }}
</template>


<script>
import { mapGetters } from 'vuex'
import prettydate from 'pretty-date'

export default {
  name: 'product-list',
  computed: mapGetters(['products']),
  methods: {
    convertDateToTimeAgo (date) {
      return prettydate.format(new Date(date))
    },
    deleteProduct (product) {
      console.log(this.products)
      this.$store.dispatch('deleteProduct', product)
    }
  },
  beforeMount () {
    this.$store.dispatch('getProducts')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
