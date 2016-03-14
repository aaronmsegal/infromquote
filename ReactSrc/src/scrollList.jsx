var React = require('react');
var ScrollButton = require('./scrollButton')

module.exports = React.createClass({
  render: function() {
    children = [];
    index = 0;
    for(i = 0; i < this.props.companies.length; i++) {
      children.push(
          <li className="scroll" key={i}>
            <ScrollButton
              symbol={this.props.companies[i][2].toUpperCase()}
              index={i}
            />
          </li>
      );
    }
    return (
      <ul className="nav nav-justified">
        {children}
      </ul>
    );
  }
});
