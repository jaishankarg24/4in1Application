var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var menuId = this.dataset.product
		var action = this.dataset.action
		console.log('menuId:', menuId, 'Action:', action)
		console.log('USER:', user)

		if (user != 'AnonymousUser'){
			updateUserOrder(menuId, action)
		}
	})
}

function updateUserOrder(menuId, action){
	console.log('User is authenticated, sending data...')

		var url = '/food_update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'menuId':menuId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

