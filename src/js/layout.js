import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import injectContext from "./store/appContext";
import { Home } from "./views/home";
import { Details } from "./views/Details";

const Layout = () => {
	const basename = process.env.BASENAME || "";

	return (
		<BrowserRouter basename={basename}>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/details/:type/:id" element={<Details />} />
				<Route path="*" element={<h1>Not found!</h1>} />
			</Routes>
		</BrowserRouter>
	);
};

export default injectContext(Layout);
