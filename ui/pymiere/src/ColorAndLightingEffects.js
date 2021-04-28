import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import LightingOptionsMenu from "./LightingOptionsMenu";
import VignetteEffectPage from "./VignetteEffectPage";
import SpecialEffectsOptions from "./SpecialEffectsOptions";
import ColorMenu from "./ColorMenu";
import TransformationEditingMenu from "./TransformationEditingMenu"

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`vertical-tabpanel-${index}`}
      aria-labelledby={`vertical-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `vertical-tab-${index}`,
    "aria-controls": `vertical-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: "flex",
    height: 900,
  },
  tabs: {
    borderRight: `1px solid ${theme.palette.divider}`,
  },
}));

// TODO Add callbacks to TabPanel child elements to save their states between tab switches
export default function ColorAndLightingEffects(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <Tabs
        orientation="vertical"
        value={value}
        onChange={handleChange}
        aria-label="Vertical tabs example"
        className={classes.tabs}
      >
        <Tab label="Color" {...a11yProps(0)} />
        <Tab label="Lighting" {...a11yProps(1)} />
        <Tab label="Special Effects" {...a11yProps(2)} />
        <Tab label="Vignette" {...a11yProps(3)} />
        <Tab label="Transformation" {...a11yProps(3)} />
      </Tabs>

      <TabPanel value={value} index={0}>
        <ColorMenu applyFilter={props.applyFilter} />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <LightingOptionsMenu applyFilter={props.applyFilter}/>
      </TabPanel>
      <TabPanel value={value} index={2}>
        <SpecialEffectsOptions applyFilter={props.applyFilter}/>
      </TabPanel>
      <TabPanel value={value} index={3}>
        <VignetteEffectPage
          getCanvas={props.getCanvas}
          setCanvas={props.setCanvas}
        />
      </TabPanel>
      <TabPanel value={value} index={4}>
        <TransformationEditingMenu
            applyFilter={props.applyFilter}
          ></TransformationEditingMenu>
      </TabPanel>

    </div>
  );
}
