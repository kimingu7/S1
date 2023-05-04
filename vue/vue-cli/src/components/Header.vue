<template>
    <div>
      <h3>Header</h3>
      <SearchBar/>
      <NaviGation/>
    </div>
  </template>
  
  <script>
  import NaviGation from '@/components/Navigation'
  import SearchBar from '@/components/Search'

  export default {
    name: 'HeaderSection',
    components :{
        NaviGation,
        SearchBar,
    }
  }
  </script>
  
  <style>
    
  </style>