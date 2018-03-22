<template>
	<nav class="nav has-shadow" style='box-shadow: 0 1px 0 rgba(219,219,219,.3);'>
	  <div class="nav-left">
	    <router-link to="/home" class="nav-item">
	      <img src="../assets/logo.png" alt="Bulma logo">
	    </router-link>
	  </div>

	  <!-- This "nav-toggle" hamburger menu is only visible on mobile -->
	  <!-- You need JavaScript to toggle the "is-active" class on "nav-menu" -->
	  <span class="nav-toggle">
	    <span></span>
	    <span></span>
	    <span></span>
	  </span>

	  <!-- This "nav-menu" is hidden on mobile -->
	  <!-- Add the modifier "is-active" to display it on mobile -->
	  <div class="nav-right nav-menu">
	    <router-link to="/makePurchase" class="nav-item is-tab" exact-active-class="is-active">
	      Shop
	    </router-link>

	    <div class="nav-item is-tab" :class="{ 'active-bottom-border': $route.path === '/makePurchase' }">
	      <div class="field is-grouped">
	        <p class="control">
	          <router-link to='/makePurchase' class="button is-info">
	            <span class="icon">
	              <i class="fa fa-shopping-cart"></i>
	            </span>
	            <span>Hello</span>
	          </router-link>
	        </p>
	      </div>
	    </div>
	  </div>
	</nav>
</template>
