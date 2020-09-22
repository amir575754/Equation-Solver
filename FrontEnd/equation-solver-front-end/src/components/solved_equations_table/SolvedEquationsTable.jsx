import React, { Component } from "react";

class SolvedEquationsTable extends Component {

    renderTableRow = (equation, equationIndex) => {
        /*
        Renders a table row given its index and information.
        */
        return (
            <tr key={equationIndex}>
                <th scope="row">{parseInt(equationIndex) + 1}</th>
                <td>{equation.original}</td>
                <td>{equation.solution}</td>
                <td>{equation.time}</td>
            </tr>
        );
    };

    renderTableRows = (equations) => {
        /*
        Renders a table given its information.
        */
        const tableRows = [];
        for (let equationIndex in equations) {
            tableRows.push(
                this.renderTableRow(equations[equationIndex], equationIndex)
            );
        }
        return tableRows;
    };

    render() {
        return (
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Original Equation</th>
                        <th scope="col">Solutions</th>
                        <th scope="col">Time to Solve</th>
                    </tr>
                </thead>
                <tbody>{this.renderTableRows(this.props.equations)}</tbody>
            </table>
        );
    }
}

export default SolvedEquationsTable;
