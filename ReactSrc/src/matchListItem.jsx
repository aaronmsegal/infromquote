var React = require('react');

module.exports = React.createClass({
  render: function() {
    symbol = this.props.symbol.toUpperCase();
    tooltip = "Add " + symbol + " to list.";
    return <li className="list-group-item search-li">
      <a href={this.props.path}>
        <button type="button"
                className="btn btn-secondary text-center search-button"
                data-toggle="tooltip"
                title= {tooltip}
                >
          <h5>{symbol}</h5>
          {this.props.name}
        </button>
      </a>
    </li>
  }
});
