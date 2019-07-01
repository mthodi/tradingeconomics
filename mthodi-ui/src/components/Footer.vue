<template>
  <v-footer height="auto" color="grey darken-4">
    <v-layout justify-center row wrap>
      <v-flex grey darken-2 py-3 text-xs-center white--text xs12>
        &copy;2019 —<strong>Martin Thodi</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>
<script>
  export default {
    name: 'Footer',
    data: () => ({
      links: [
        'Home',
        'About Us'
      ]
    })
  }
