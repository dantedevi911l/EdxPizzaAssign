

document.addEventListener('DOMContentLoaded', () => {
   console.log(pizzas);
   var toppings_id = document.querySelector('#toppings');
   //toppings_id.style.display = 'none';


   for(type in pizzas){
      for(sub_type in pizzas[type]){
         var selectedId = document.querySelector("#"+type.replace(' ','')+"_"+sub_type.replace(' ','')+"_"+"select");
         var priceId = document.querySelector("#"+type.replace(' ','')+"_"+sub_type.replace(' ','')+"_"+"price");
         priceId.innerHTML = "$"+pizzas[type][sub_type][0]['Small'];
         selectedId.addEventListener( "click", togglePrice.bind(this, [type, sub_type]) );

      }
   }

   function togglePrice(args, event){
      //args[0] is the type
      //args[1] is the sub_type
      console.log(args[0]+"_"+args[1]);
      // change the price in the span class of the button assuming zero toppings
      document.querySelector("#"+args[0].replace(' ','')+"_"+args[1].replace(' ','')+"_"+"price").innerHTML = "$"+pizzas[args[0]][args[1]][0][event.target.value];

   }
});
