<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col
          v-for="(store, i) in allStores"
          :key="i"
          align-self="center"
      >
        <v-card
            selectable
            @click="openStoreAnalysis(store)"
            class="imageHover"
            style="border-radius: 10px"
            max-width="20vw">
          <v-img
              :src="store.logo"
              :alt="`${store.description}`"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.2), rgba(255,255,255,.2)">
            <v-card-title>{{ store.name }}</v-card-title>
            <v-card-subtitle></v-card-subtitle>
          </v-img>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "BaseListStores",
  data() {
    return {
      allStores: [],
    }
  },
  computed: {
    ...mapGetters("stores", ["getAllStores"]),
  },
  mounted() {
    this.allStores = this.getAllStores
  },
  methods: {
    openStoreAnalysis(store) {
      console.log("Open")
      console.log(store)
      this.$router.push({name: "chart", query: {storeId: store}})
    }
  }
}
</script>

<style scoped>
.imageHover:hover {
  -webkit-transition: transform 0.6s ease-in;
  transform: scale(1.1);
  z-index: 2;
}

.imageHover:not( :hover){
  -webkit-transition: transform 0.6s ease-out;
}

</style>
