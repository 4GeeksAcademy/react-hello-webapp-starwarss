import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

export const Details = () => {
	const { type, id } = useParams();
	const navigate = useNavigate();
	const [details, setDetails] = useState(null);

	// Função para buscar detalhes do item
	const fetchDetails = async () => {
		try {
			const response = await fetch(`https://www.swapi.tech/api/${type}/${id}`);
			const data = await response.json();
			setDetails(data.result.properties);
		} catch (error) {
			console.error("Erro ao buscar detalhes:", error);
		}
	};

	useEffect(() => {
		fetchDetails();
	}, [type, id]);

	if (!details) return <p>Loading...</p>;

	// Função para definir as propriedades exibidas de forma personalizada
	const renderDetails = () => {
		if (type === "people") {
			return (
				<>
					<p><strong>Height:</strong> {details.height}</p>
					<p><strong>Mass:</strong> {details.mass}</p>
					<p><strong>Hair Color:</strong> {details.hair_color}</p>
					<p><strong>Skin Color:</strong> {details.skin_color}</p>
					<p><strong>Eye Color:</strong> {details.eye_color}</p>
					<p><strong>Birth Year:</strong> {details.birth_year}</p>
					<p><strong>Gender:</strong> {details.gender}</p>
				</>
			);
		} else if (type === "vehicles") {
			return (
				<>
					<p><strong>Model:</strong> {details.model}</p>
					<p><strong>Manufacturer:</strong> {details.manufacturer}</p>
					<p><strong>Passengers:</strong> {details.passengers}</p>
					<p><strong>Crew:</strong> {details.crew}</p>
					<p><strong>Length:</strong> {details.length}</p>
					<p><strong>Max Speed:</strong> {details.max_atmosphering_speed}</p>
				</>
			);
		} else if (type === "planets") {
			return (
				<>
					<p><strong>Climate:</strong> {details.climate}</p>
					<p><strong>Gravity:</strong> {details.gravity}</p>
					<p><strong>Terrain:</strong> {details.terrain}</p>
					<p><strong>Population:</strong> {details.population}</p>
					<p><strong>Diameter:</strong> {details.diameter}</p>
					<p><strong>Orbital Period:</strong> {details.orbital_period}</p>
					<p><strong>Rotation Period:</strong> {details.rotation_period}</p>
				</>
			);
		} else {
			return <p>Information not available</p>;
		}
	};

	return (
		<div className="container mt-5">
			<button className="btn btn-secondary btn-back mb-3" onClick={() => navigate(-1)}>
				← Back
			</button>

			<h1 className="text-center">{details.name}</h1>
			{renderDetails()}
		</div>
	);
};
