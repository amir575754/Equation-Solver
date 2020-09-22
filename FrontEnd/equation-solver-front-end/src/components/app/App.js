import React, { Component } from "react";
import EquationSolver from "..\\equation_solver\\EquationSolver";
import SolvedEquationsTable from "..\\solved_equations_table\\SolvedEquationsTable";

class App extends Component {
	SERVER_IP = "localhost";
	SERVER_PORT = 5000;
	TIMEOUT = 1000;
	EQUATIONS_URL = `http://${this.SERVER_IP}:${this.SERVER_PORT}/equations`;


	constructor() {
		super();
		// Assign some random value, so we can use setState() in the updateEquationHistory().
		this.state = {
			some: ''
		};
	}

	componentDidMount() {
		/*
		When the component is mounted, bind the update methods
		and set the interval to update the equation history every 1 second.
		*/
		this.fetchEquationHistory = this.fetchEquationHistory.bind(this);
		this.updateEquationHistory = this.updateEquationHistory.bind(this);
		setInterval(this.updateEquationHistory, this.TIMEOUT);
	};

	async fetchEquationHistory() {
		/*
		Fetch the equation history from the server and return it
		*/
		let data = { equations: [] };
		try {
			const response = await fetch(this.EQUATIONS_URL);
			data = await response.json();
		} catch (error) {
			console.log("An error occurred when sending the new equation");
		}
		return data;

	};

	async updateEquationHistory() {
		/*
		Fetch the equation history from the server, and update it
		in SolvedEquationsTable's state.
		*/
		const data = await this.fetchEquationHistory();
		this.setState({ equations: data.equations });
		console.log("Updated!");
	};

	render() {
		return (
			<div className="jumbotron text-center">
				<EquationSolver></EquationSolver>
				<SolvedEquationsTable
					equations={this.state.equations}
				></SolvedEquationsTable>
			</div>
		);
	}
}

export default App;
