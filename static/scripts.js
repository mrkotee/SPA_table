
//$(document).ready(function(){
//    $('select[name=page]').change(function(){
//        $.ajax({
//        url:"/",
//        type: "POST",
//        data: {"page": this.selectedIndex,
//                "per_page": $('select[name=per_page]').val()},
//        contentType: "application/json;charset=UTF-8"
//                }).done(function( data ) {
//                              if ( console && console.log ) {
//                                console.log( "Sample of data:", data );
//                              }
//                              });
//    });
//});
new Vue({
  el: "select[name=page]",
  data: {
    key: "",
  },
  methods: {
  	onchange: function() {
    	console.log(this.key)
    	axios.post("/"), {
    	page: this.key,

    	}
      alert(this.key)
    }
  }
})
