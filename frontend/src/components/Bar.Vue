<head>
    <meta charset="utf-8">
    <title>Simple vueshop</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/spectre.css/0.2.14/spectre.min.css">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>


<template>
  <div id="app">
    <header>
      <ul>
        <li><i class="fa fa-cloud" style="font-size:300%;color:lightblue;"></i></li>
        <li><router-link to="/home" class="nav-item is-tab" exact-active-class="is-active">+ Home</router-link></li>
        <li><router-link to="/makePurchase" class="nav-item is-tab" exact-active-class="is-active">+ Make purchase</router-link></li>
        <li style="float:right"><router-link to="/makePurchase" class="nav-item is-tab" exact-active-class="is-active"><i class="fa fa-shopping-cart" style="font-size:300%;color:darkred;"></i></router-link></li>
      </ul>
    </header>
  </div>
</template>

<script>
import CreateProduct from './CreateProduct'
import ProductsInOrderList from './ProductsInOrderList'

export default {
  name: 'app',
  components: {
    'create-product': CreateProduct,
    'productorder-list': ProductsInOrderList
  }

}
</script>

<style>
      ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #333;
      }

      li {
      float: left;
      }

      li a, router-link {
      display: block;
      color: white;
      text-align: center;
      padding: 6px 16px;
      text-decoration: none;
      }

      li a:hover:not(.active) {
      background-color: #111;
      }

      li router-link:hover:not(.active) {
      background-color: #111;
      }

      .active {
      background-color: #4CAF50;
      }
</style>
