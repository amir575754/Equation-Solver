import React, { Component } from "react";
import EquationSolver from "..\\equation_solver\\EquationSolver";
import SolvedEquationsTable from "..\\solved_equations_table\\SolvedEquationsTable";

class App extends Component {
	constructor() {
		super();
		this.state = {
			equations: [
				{ original: "BlaBla", solved: "BlaBla2", time: 15 },
				{ original: "BlaBla", solved: "BlaBla2", time: 15 },
				{ original: "BlaBla", solved: "BlaBla2", time: 15 },
				{ original: "BlaBla", solved: "BlaBla2", time: 15 }
			]
		};
	}

	updateEquations = () => {
		// TODO: Replace with code to update the equations from the server
		const newEquations = [];
		this.setState({ equations: newEquations });
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
