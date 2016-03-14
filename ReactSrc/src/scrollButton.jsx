var React = require('react');

module.exports = React.createClass({
  clicked : function() {
    list = document.getElementById("company-scrool-list");
    if(list)
      list.scrollLeft = 508 * this.props.index;
  },
  render: function() {
    tooltip = "Focus on " + this.props.symbol
    return (
      <button type="button"
        className="btn btn-default scroll"
        aria-label="Left Align"
        onClick={this.clicked}
        data-toggle="tooltip"
        title={tooltip}
        >
        {this.props.symbol}
      </button>
    );
  }
});
