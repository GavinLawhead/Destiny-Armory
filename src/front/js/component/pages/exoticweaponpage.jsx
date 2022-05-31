import React, { useState, useContext } from "react";
import ReactPlayer from "react-player";
import { Context } from "../../store/appContext";

export const ExoticWeaponPage = () => {
  const { store, actions } = useContext(Context);
  console.log(window.location.href);
  let par = store.singleExoticWeapon.location_video;
  return (
    <div
      className="card"
      style={{
        position: "relative",
        marginLeft: "10%",
        marginRight: "10%",
        // marginBottom: "10%",
      }}
    >
      <img
        style={{ width: "25%", paddingLeft: "2%", paddingTop: "2%" }}
        src={store.singleExoticWeapon.weapon_Img}
      />
      <div
        style={{ position: "absolute", paddingLeft: "27%", paddingTop: "3%" }}
      >
        <p>{store.singleExoticWeapon.weapon_name}</p>
        <p>{store.singleExoticWeapon.weapon_lore}</p>
        <p>{store.singleExoticWeapon.weapon_type}</p>
      </div>
      <p style={{ position: "relative", paddingTop: "3%", paddingLeft: "3%" }}>
        {store.singleExoticWeapon.location_description}
      </p>
      <div
        style={{
          position: "relative",
          paddingLeft: "65.5%",
          paddingTop: "5%",
          paddingBottom: "",
        }}
      >
        {store.singleExoticWeapon.location_video == null ? (
          <div>
            <p>hello world</p>
          </div>
        ) : (
          <>
            <ReactPlayer
              controls
              url={store.singleExoticWeapon.location_video}
            />
            <p style={{ paddingLeft: "73%" }}>
              {store.singleExoticWeapon.video_credit}
            </p>
            <button
              // onClick={() => navigator.clickport.writeText(window.location.href)}
              onClick={() => navigator.clipboard.writeText(par)}
            >
              copy
            </button>
          </>
        )}
      </div>
    </div>
  );
};
