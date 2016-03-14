var React = require('react');

module.exports = React.createClass({
  getInitialState: function() {
    return {
      text: this.props.text
    }
  },
  handleInputChange: function(event) {
    this.props.onInput(event.target.value);
  },
  render: function() {
    return (
        <input
          value={this.props.text}
          onChange={this.handleInputChange}
          type="text"
          className="form-control"
          placeholder="Search"
          id="search-text-box"
        />
    );
  }
});
