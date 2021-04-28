import React, { Component } from 'react';
import FileMenu from './TopBarFileMenu'
import './TopLevelToolbar.css'


class TopLevelToolbar extends Component {

  render() {
    return (
      <div id="topBar">
        {/*<div class="menuButton"><FileMenu title="File"/></div>*/}
        {/*<div class="menuButton"><CustomizedMenus title="Menu"/></div>*/}
        {/*<div class="menuButton"><CustomizedMenus title="Effects"/></div>*/}
      </div>
    );
  }
}

export default TopLevelToolbar;