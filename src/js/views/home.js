import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/styles.css";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [characters, setCharacters] = useState([]);
	const [vehicles, setVehicles] = useState([]);
	const [planets, setPlanets] = useState([]);

	const fetchCharacters = async () => {
		const response = await fetch("https://www.swapi.tech/api/people");
		const data = await response.json();
		setCharacters(data.results);
		localStorage.setItem("characters", JSON.stringify(data.results));
	};

	const fetchVehicles = async () => {
		const response = await fetch("https://www.swapi.tech/api/vehicles");
		const data = await response.json();
		setVehicles(data.results);
		localStorage.setItem("vehicles", JSON.stringify(data.results));
	};

	const fetchPlanets = async () => {
		const response = await fetch("https://www.swapi.tech/api/planets");
		const data = await response.json();
		setPlanets(data.results);
		localStorage.setItem("planets", JSON.stringify(data.results));
	};

	useEffect(() => {
		const storedCharacters = localStorage.getItem("characters");
		const storedVehicles = localStorage.getItem("vehicles");
		const storedPlanets = localStorage.getItem("planets");

		if (storedCharacters) {
			setCharacters(JSON.parse(storedCharacters));
		} else {
			fetchCharacters();
		}

		if (storedVehicles) {
			setVehicles(JSON.parse(storedVehicles));
		} else {
			fetchVehicles();
		}

		if (storedPlanets) {
			setPlanets(JSON.parse(storedPlanets));
		} else {
			fetchPlanets();
		}
	}, []);

	return (
		<div className="container mt-5">
			{/* StarWars-logo */}
			<div className="logo-container">
				<img src="https://upload.wikimedia.org/wikipedia/commons/6/6c/Star_Wars_Logo.svg" alt="Star Wars Logo" className="logo" />
			</div>

			<h2>My favorites</h2>
			<div className="row">
				{store.favorites.map((fav, index) => (
					<div className="col-md-3 mb-4" key={index}>
						<div className="card">
							<div className="card-body">
								<h5>{fav}</h5>
								<button
									className="btn btn-danger"
									onClick={() => actions.removeFavorite(fav)}
								>Remover</button>
							</div>
						</div>
					</div>
				))}
			</div>

			<h1>Characters</h1>
			<div className="row">
				{characters.map((character, index) => (
					<div className="col-md-4 mb-4" key={index}>
						<div className="card">
							<img src={`https://starwars-visualguide.com/assets/img/characters/${character.uid}.jpg`} alt={character.name} />
							<div className="card-body">
								<h5>{character.name}</h5>
								<button
									className="btn btn-learn-more"
									onClick={() => window.location.href = `/details/people/${character.uid}`}
								>
									Learn More
								</button>
								<button
									className={`btn btn-favorite ${store.favorites.includes(character.name) ? 'pressed' : ''}`}
									onClick={() => actions.toggleFavorite(character.name)}
								>
									{store.favorites.includes(character.name)
										? <i className="fa fa-heart"></i>
										: <i className="fa fa-heart-o">♥</i>}
								</button>
							</div>
						</div>
					</div>
				))}
			</div>

			<h1>Vehicles</h1>
			<div className="row">
				{vehicles.map((vehicle, index) => (
					<div className="col-md-4 mb-4" key={index}>
						<div className="card">
							<img src={`https://starwars-visualguide.com/assets/img/vehicles/${vehicle.uid}.jpg`} alt={vehicle.name} />
							<div className="card-body">
								<h5>{vehicle.name}</h5>
								<button
									className="btn btn-learn-more"
									onClick={() => window.location.href = `/details/vehicles/${vehicle.uid}`}
								>
									Learn More
								</button>
								<button
									className={`btn btn-favorite ${store.favorites.includes(vehicle.name) ? 'pressed' : ''}`}
									onClick={() => actions.toggleFavorite(vehicle.name)}
								>
									{store.favorites.includes(vehicle.name)
										? <i className="fa fa-heart"></i>
										: <i className="fa fa-heart-o">♥</i>}
								</button>
							</div>
						</div>
					</div>
				))}
			</div>

			<h1>Planets</h1>
			<div className="row">
				{planets.map((planet, index) => (
					<div className="col-md-4 mb-4" key={index}>
						<div className="card">
							<img src={`https://starwars-visualguide.com/assets/img/planets/${planet.uid}.jpg`} alt={planet.name} />
							<div className="card-body">
								<h5>{planet.name}</h5>
								<button
									className="btn btn-learn-more"
									onClick={() => window.location.href = `/details/planets/${planet.uid}`}
								>
									Learn More
								</button>
								<button
									className={`btn btn-favorite ${store.favorites.includes(planet.name) ? 'pressed' : ''}`}
									onClick={() => actions.toggleFavorite(planet.name)}
								>
									{store.favorites.includes(planet.name)
										? <i className="fa fa-heart"></i>
										: <i className="fa fa-heart-o">♥</i>}
								</button>
							</div>
						</div>
					</div>
				))}
			</div>
		</div>
	);
};