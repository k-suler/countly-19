<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col
          v-for="(store, i) in allStores"
          :key="i"
          align-self="center"
          cols="12"
          sm="6"
      >
        <v-card
            selectable
            @click="openStoreAnalysis(store)"
            class="imageHover"
            style="border-radius: 10px"

            >
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
    console.log(this.getAllStores)
  },
  methods: {
    openStoreAnalysis(store) {
      console.log(store)
      this.$router.push({name: "chart", params: {storeId: store.storeId}})
    }
  }
}
</script>

<style scoped>
.imageHover:hover {
  -webkit-transition: transform 0.3s ease-in;
  transform: scale(1.1);
  z-index: 2;
}

.imageHover:not( :hover){
  -webkit-transition: transform 0.3s ease-out;
}

</style>
