import React, { Component } from "react";

class EquationSolver extends Component {
    SERVER_IP = "localhost";
    SERVER_PORT = 5000;
    UPLOAD_EQUATION_URL = `http://${this.SERVER_IP}:${this.SERVER_PORT}/upload_equation/`;

    handleSolveClick = () => {
        /*
        When the solve button is clicked, takes the equation from equationInput,
        removes all redundant characters and sends it to the backend
        to be processes and solved.
        */
        const equationInput = document.getElementById("equationInput");
        const equationValue = this.removeRedundantCharacters(equationInput.value);
        equationInput.value = "";
        this.sendEquationToServer(equationValue);
        console.log(equationValue, "Done!");
    };

    handleDeleteClick = () => {
        /*
        When the delete button is clicked, it deletes the text
        from the equation input.
        */
        const equationInput = document.getElementById("equationInput");
        equationInput.value = "";
    };

    sendEquationToServer = async function (equation) {
        let response = await fetch(`${this.UPLOAD_EQUATION_URL}${equation}`);
        let data = await response.text();
        console.log(data, "Sent");
    };

    removeRedundantCharacters = (expression) => {
        /*
        Removes all spaces from the equations and replaces the sign of power
        with python's sign of power. Returns the new expression.
        */
        return expression.replaceAll(" ", "").replaceAll("^", "**");
    };


    render() {
        return (
            <div>
                <div className="input-group mb-3">
                    <div className="input-group-prepend">
                        <span className="input-group-text" id="basic-addon1">
                            Enter your equation here
                        </span>
                    </div>
                    <input
                        id="equationInput"
                        type="text"
                        className="form-control"
                        placeholder="Equation"
                        aria-label="Equation"
                        aria-describedby="basic-addon1"
                    ></input>
                </div>
                <button onClick={this.handleSolveClick} type="button" className="btn btn-lg btn-primary m-3">
                    Solve
                </button>
                <button onClick={this.handleDeleteClick} type="button" className="btn btn-lg btn-danger m-3">
                    Delete
                </button>
            </div>
        );
    }
}

export default EquationSolver;
