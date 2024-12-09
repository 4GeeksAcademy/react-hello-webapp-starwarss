const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			favorites: [] // Estado inicial para favoritos
		},
		actions: {
			// Add/remover um personagem dos favoritos
			toggleFavorite: (name) => {
				const store = getStore();
				const favorites = store.favorites.includes(name)
					? store.favorites.filter(fav => fav !== name) // Remove se já estiver nos favoritos
					: [...store.favorites, name]; // Adiciona se não estiver
				
				setStore({ favorites }); // Atualiza o estado global
			},

			// Remove um favorito específico
			removeFavorite: (name) => {
				const store = getStore();
				const updatedFavorites = store.favorites.filter(fav => fav !== name);
				setStore({ favorites: updatedFavorites }); // Atualiza o estado global
			},

			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			loadSomeData: () => {
				
			},

			changeColor: (index, color) => {
				const store = getStore();
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
