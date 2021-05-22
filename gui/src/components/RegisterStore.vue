<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Registracija trgovine</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-store"
                name="login"
                v-model="formData.name"
                label="Name of store"
                type="text"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-counter"
                name="login"
                v-model="formData.maxNumberOfCustomers"
                label="Email"
                type="text"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-text"
                name="password"
                v-model="formData.description"
                label="Opis"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="signup">
              Pošlji &nbsp;
              <v-icon>mdi-send</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    formData: {
      name: "test",
      maxNumberOfCustomers: 0,
      description: "",
    },
  }),
  methods: {
    signup() {
      this.$store.dispatch("store/registerStore", this.formData);
    },
  },
};
</script>

<style scoped></style>
